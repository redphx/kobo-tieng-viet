#pragma once

#include <QWidget>
#include <QMap>
#include <QSize>

#ifndef DELETE_FILE_PATH
	#define DELETE_FILE_PATH "/mnt/onboard/.adds/tiengviet/uninstall.txt"
#endif

typedef QWidget VirtualKey;
typedef QWidget VirtualKeyboard;
typedef VirtualKeyboard PopupKeyboard;
typedef QWidget NickelTouchMenu;
typedef QWidget SearchKeyboardController;
typedef QWidget PopupKeyboardController;

struct KeyboardLayoutRow {
    QVector<VirtualKey*> keys;
    float leftSpacer = 0;
    float rightSpacer = 0;
};

void (*SearchKeyboardController_popupKeyboard)(SearchKeyboardController* self, VirtualKey* key, QVector<KeyboardLayoutRow> rows);
void (*PopupKeyboardController_constructor)(PopupKeyboardController* self, QWidget* parent, VirtualKeyboard* keyboard, QVector<KeyboardLayoutRow> rows);
VirtualKey* (*SearchKeyboardController_newKey)(SearchKeyboardController* self, const char* label, int keyId, int weight);
NickelTouchMenu* (*PopupKeyboardController_menu)(PopupKeyboardController* self);
int (*VirtualKey_text)(VirtualKey* self);
QSize* (*VirtualKeyboard_keySize)(VirtualKeyboard* self);

using KeyRow = std::vector<const char*>;
using KeyRows = std::vector<KeyRow>;

const QMap<QString, KeyRows> KEYBOARD_POPUP_MAP = {
	// A
	{"a", {
		{"â", "ấ", "ầ", "ẩ", "ẫ", "ậ"},
		{"ă", "ắ", "ằ", "ẳ", "ẵ", "ặ"},
		{ "", "á", "à", "ả", "ã", "ạ"},
	}},
	{"A", {
		{"Â", "Ấ", "Ầ", "Ẩ", "Ẫ", "Ậ"},
		{"Ă", "Ắ", "Ằ", "Ẳ", "Ẵ", "Ặ"},
		{ "", "Á", "À", "Ả", "Ã", "Ạ"},
	}},

	// E
	{"e", {
		{"ê", "ế", "ề", "ể", "ễ", "ệ"},
		{ "", "é", "è", "ẻ", "ẽ", "ẹ"},
	}},
	{"E", {
		{"Ê", "Ế", "Ề", "Ể", "Ễ", "Ệ"},
		{ "", "É", "È", "Ẻ", "Ẽ", "Ẹ"},
	}},

	// U
	{"i", {
		{"í", "ì", "ỉ", "ĩ", "ị"},
	}},
	{"I", {
		{"Í", "Ì", "Ỉ", "Ĩ", "Ị"},
	}},

	// O
	{"o", {
		{"ô", "ố", "ồ", "ổ", "ỗ", "ộ"},
		{"ơ", "ớ", "ờ", "ở", "ỡ", "ợ"},
		{ "", "ó", "ò", "ỏ", "õ", "ọ"},
	}},
	{"O", {
		{"Ô", "Ố", "Ồ", "Ổ", "Ỗ", "Ộ"},
		{"Ơ", "Ớ", "Ờ", "Ở", "Ỡ", "Ợ"},
		{ "", "Ó", "Ò", "Ỏ", "Õ", "Ọ"},
	}},

	// U
	{"u", {
		{"ư", "ứ", "ừ", "ử", "ữ", "ự"},
		{ "", "ú", "ù", "ủ", "ũ", "ụ"},
	}},
	{"U", {
		{"Ư", "Ứ", "Ừ", "Ử", "Ữ", "Ự"},
		{ "", "Ú", "Ù", "Ủ", "Ũ", "Ụ"},
	}},

	// Y
	{"y", {
		{"ý", "ỳ", "ỷ", "ỹ", "ỵ"},
	}},
	{"Y", {
		{"Ý", "Ỳ", "Ỷ", "Ỹ", "Ỵ"},
	}},
};
