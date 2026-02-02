#include "tiengviet.h"
#include <NickelHook.h>

#include <QString>
#include <QVector>
#include <QLocale>
#include <QPointer>
#include <QVBoxLayout>
#include <QHBoxLayout>

struct nh_info PluginInfo = {
    .name = "TiengViet",
    .desc = "Vietnamese keyboard",
    .uninstall_flag = DELETE_FILE_PATH,
    // .uninstall_xflag = NULL,
    // .failsafe_delay = 3,
};

int pluginInit() {
    return 0;
}

bool pluginInstall() {
    return true;
}

struct nh_hook PluginHook[] = {
    {
        .sym      = "_ZN24SearchKeyboardController13popupKeyboardEP10VirtualKey7QVectorI17KeyboardLayoutRowE",
        .sym_new  = "hook_SearchKeyboardController_popupKeyboard",
        .lib      = "libnickel.so.1.0.0",
        .out      = nh_symoutptr(SearchKeyboardController_popupKeyboard),
        .desc     = "SearchKeyboardController::popupKeyboard()",
        .optional = true,
    },
    {
        .sym      = "_ZN23PopupKeyboardControllerC1EP26ExtendedKeyboardControllerP15VirtualKeyboard7QVectorI17KeyboardLayoutRowE",
        .sym_new  = "hook_PopupKeyboardController_constructor",
        .lib      = "libnickel.so.1.0.0",
        .out      = nh_symoutptr(PopupKeyboardController_constructor),
        .desc     = "PopupKeyboardController::constructor()",
        .optional = true,
    },
    {0}
};

struct nh_dlsym PluginsDlsym[] = {
    {
		.name     = "_ZNK24SearchKeyboardController6newKeyEPKcii",
		.out      = nh_symoutptr(SearchKeyboardController_newKey),
        .desc     = "SearchKeyboardController::newKey()",
        .optional = true,
	},
    {
        .name     = "_ZNK10VirtualKey4textEv",
        .out      = nh_symoutptr(VirtualKey_text),
        .desc     = "VirtualKey::text()",
        .optional = true,
    },
    {
        .name     = "_ZN23PopupKeyboardController4menuEv",
        .out      = nh_symoutptr(PopupKeyboardController_menu),
        .desc     = "PopupKeyboardController::menu()",
        .optional = true,
    },
    {
        .name     = "_ZNK15VirtualKeyboard7keySizeEv",
		.out      = nh_symoutptr(VirtualKeyboard_keySize),
        .desc     = "VirtualKeyboard::keySize()",
        .optional = true,
    },
	{0}
};

NickelHook(
    .init      = &pluginInit,
    .info      = &PluginInfo,
    .hook      = PluginHook,
    .dlsym     = PluginsDlsym,
    .uninstall = &pluginInstall,
);

QPointer<QWidget> globalPopupKeyboardController = nullptr;

extern "C" __attribute__((visibility("default")))
void hook_SearchKeyboardController_popupKeyboard(SearchKeyboardController* self, VirtualKey* key, QVector<KeyboardLayoutRow> rows) {
    // Kobo only renders the first row of keys correctly (the rest are inserted into PopupKeyboard without wrapping inside a layout)
    // To fix this, we only let Kobo render the first row. But we also put other rows as empty lists so the popup is prepared correctly
    QVector<KeyboardLayoutRow> additionalRows;
    const QString& label = *reinterpret_cast<QString*>(VirtualKey_text(key));

    // Get custom popup keys
    if (KEYBOARD_POPUP_MAP.contains(label)) {
        // Remove old keys
        rows.clear();

        int i = -1;
        auto popupRows = KEYBOARD_POPUP_MAP.value(label);
        for (const auto& popupRow : popupRows) {
            ++i;
            KeyboardLayoutRow keysRow;

            // keyId (0xffff0000) can be the same for every keys, as long as it's not from special keys
            for (const char* keyLabel : popupRow) {
                keysRow.keys.append(SearchKeyboardController_newKey(self, keyLabel,  0xffff0000, 10));
            }

            if (i == 0) {
                rows.append(keysRow);
            } else {
                // Add empty row so Kobo increases NickelTouchMenu's height
                rows.append(KeyboardLayoutRow());
                additionalRows.append(keysRow);
            }
        }
    }

    // Let Kobo setup the keys
    SearchKeyboardController_popupKeyboard(self, key, rows);

    if (additionalRows.isEmpty() || !globalPopupKeyboardController || !PopupKeyboardController_menu) {
        globalPopupKeyboardController = nullptr;
        return;
    }

    NickelTouchMenu* menu = PopupKeyboardController_menu(globalPopupKeyboardController);
    globalPopupKeyboardController = nullptr;

    PopupKeyboard* popupKeyboard = menu->findChild<PopupKeyboard*>(QString());
    if (!popupKeyboard) {
        return;
    }

    int rowsCount = additionalRows.size();
    QSize* keySize = VirtualKeyboard_keySize(popupKeyboard);
    QVBoxLayout* rootLayout = qobject_cast<QVBoxLayout*>(popupKeyboard->layout());
    // Disable layout updates
    rootLayout->setEnabled(false);
    rootLayout->setSpacing(0);

    for (int i = 0; i < rowsCount; ++i) {
        QHBoxLayout* hRow = new QHBoxLayout();
        hRow->setContentsMargins(0, 0, 0, 0);
        hRow->setSpacing(0);

        // Add every key in this row to the horizontal layout
        const QVector<VirtualKey*>& keys = additionalRows[i].keys;
        for (VirtualKey* k : keys) {
            k->setContentsMargins(0, 0, 0, 0);
            k->setFixedSize(*keySize);

            hRow->addWidget(k);
        }

        rootLayout->addLayout(hRow);
    }

    // Enable layout updates again
    rootLayout->setEnabled(true);
    // Increate popup's height
    popupKeyboard->setFixedSize(popupKeyboard->width(), popupKeyboard->height() * (1 + rowsCount));
};

extern "C" __attribute__((visibility("default")))
void hook_PopupKeyboardController_constructor(PopupKeyboardController* self, QWidget* parent, VirtualKeyboard* keyboard, QVector<KeyboardLayoutRow> rows) {
    PopupKeyboardController_constructor(self, parent, keyboard, rows);
    // save PopupKeyboardController instance so it can be used in SearchKeyboardController_popupKeyboard
    globalPopupKeyboardController = self;
}
