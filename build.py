import re
from datetime import date
import argparse
import os
import html
import shutil
from fontTools.ttLib import TTFont
import tarfile
from pathlib import Path
import subprocess
from dotenv import load_dotenv


load_dotenv()
CURRENT_DIR = Path(__file__).resolve().parent
KOBOROOT_DIR = CURRENT_DIR / 'KoboRoot'

FONT_WEIGHT_MAP = {
    'regular': '',
    'italic': 'Italic',
    'bold': 'Bold',
    'bold-italic': 'BoldItalic',
}

FONTS = {
    'sans': {
        'Avenir Next': {
            # style: [font file name, font name, font style]
            'regular': ['Avenir', 'AvenirNext-Regular'],
            'italic': ['Avenir-Italic', 'AvenirNext-Italic'],
            'bold': ['Avenir-Bold', 'AvenirNext-Bold'],
            'bold-italic': ['Avenir-BoldItalic', 'AvenirNext-BoldItalic'],
        },
        'Rakuten Sans': {
            'regular': ['RakutenSansUIApp-Regular', 'RakutenSansUI', 'UI'],
            'italic': ['RakutenSansUIApp-Italic', 'RakutenSansUI_it', 'UI_it'],
            'bold': ['RakutenSansUIApp-Bold', 'RakutenSansUI_bold', 'UI_bold'],
            'bold-italic': [
                'RakutenSansUIApp-BoldItalic',
                'RakutenSansUI_bold_it',
                'UI_bold_it',
            ],
        },
    },
    'serif': {
        'Georgia': {
            'regular': ['georgia', 'Georgia'],
            'italic': ['georgiai', 'Georgia-Italic'],
            'bold': ['georgiab', 'Georgia-Bold'],
            'bold-italic': ['georgiaz', 'Georgia-BoldItalic'],
        },
        'Rakuten Serif': {
            'regular': ['RakutenSerifApp-Regular', 'RakutenSerif'],
            'italic': ['RakutenSerifApp-Italic', 'RakutenSerif_it'],
            'bold': ['RakutenSerifApp-Bold', 'RakutenSerif_bold'],
            'bold-italic': ['RakutenSerifApp-BoldItalic', 'RakutenSerif_bold_it'],
        },
    },
    'mono': {
        # Mono font must have the "Courier " prefix
        'Courier': {
            'regular': ['Courier Mono-Regular', 'Courier Regular'],
            'italic': ['Courier Mono-Italic', 'Courier Italic'],
            'bold': ['Courier Mono-Bold', 'Courier Bold'],
            'bold-italic': ['Courier Mono-BoldItalic', 'Courier BoldItalic'],
        },
    },
}


def copy_fonts():
    FONTS_SOURCE_DIR = './fonts'
    FONTS_TROLLTECH_DIR = (
        Path(KOBOROOT_DIR)
        / 'usr'
        / 'local'
        / 'Trolltech'
        / 'QtEmbedded-4.6.2-arm'
        / 'lib'
        / 'fonts'
    )
    FONTS_ONBOARD_DIR = Path(KOBOROOT_DIR) / 'mnt' / 'onboard' / 'fonts'

    # Generate font dirs
    os.makedirs(FONTS_TROLLTECH_DIR, exist_ok=True)
    os.makedirs(FONTS_ONBOARD_DIR, exist_ok=True)

    # Copy fonts
    for font_class in FONTS:
        font_def = FONTS[font_class]

        for family_name in font_def:
            for style, info in font_def[family_name].items():
                # Copy font to the target location
                source_path = Path(FONTS_SOURCE_DIR) / f'{font_class}-{style}.ttf'

                if font_class == 'mono':
                    output_path = Path(FONTS_ONBOARD_DIR) / f'{info[0]}.ttf'
                else:
                    output_path = Path(FONTS_TROLLTECH_DIR) / f'{info[0]}.ttf'

                shutil.copy(source_path, output_path)

                # Edit font metadata
                font = TTFont(output_path)
                name_table = font['name']

                for record in name_table.names:
                    if record.nameID == 1:  # Font Family Name
                        record.string = family_name
                    elif record.nameID == 2:  # Style
                        if len(info) >= 3:
                            record.string = info[2]
                    elif record.nameID == 4:  # Name for Humans
                        record.string = (
                            family_name + ' ' + FONT_WEIGHT_MAP[style]
                        ).strip()
                    elif record.nameID == 6:  # Font name
                        record.string = info[1]

                font.save(output_path)

    print(f'- Đã chép font vào thư mục {FONTS_TROLLTECH_DIR}')


def inject_about_page(source: str, version: str):
    # Find the index of "<p>© 2009-" string
    index = source.index('<source>&lt;p&gt;&amp;copy; 2009-%1')
    # Find the closest <translation> tag
    index = source.index('<translation>', index) + 13

    info = [
        f'<p><b>Dự án Kobo tiếng Việt</b> ({version})</p>',
        '<p><i>github.com/redphx/kobo-tieng-viet</i></p>',
        '<br>',
    ]

    # Inject project's info
    info = ''.join(info)
    info = html.escape(info, quote=False)
    source = source[:index] + info + source[index:]

    return source


def combine_translations(version: str):
    dir_path = Path(CURRENT_DIR) / 'translation' / 'contexts'

    combined_text = '''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="vi_VN">
'''

    for fname in os.listdir(dir_path):
        if not fname.endswith('.xml'):
            continue

        file_path = Path(dir_path) / fname
        with open(file_path, 'r', encoding='utf-8') as f:
            combined_text += f.read() + '\n'

    combined_text += '</TS>'

    # Add info into the About page
    combined_text = inject_about_page(combined_text, version)

    # Save .ts file
    output_path = Path(CURRENT_DIR) / 'trans_vi.ts'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(combined_text)

    # Convert .ts to .qm
    qm_path = (
        Path(KOBOROOT_DIR) / 'usr' / 'local' / 'Kobo' / 'translations' / 'trans_vi.qm'
    )
    os.makedirs(qm_path.parent, exist_ok=True)
    lrelease_path = os.environ['LRELEASE']
    subprocess.run([lrelease_path, 'trans_vi.ts', '-qm', qm_path])

    # Delete .ts file
    os.remove(output_path)

    print(f'- Đã tạo file {qm_path} thành công')


def generate_tgz(version: str):
    dist_path = Path(CURRENT_DIR) / 'dist'
    os.makedirs(dist_path, exist_ok=True)

    # Create dist/KoboRoot.tgz
    with tarfile.open(dist_path / 'KoboRoot.tgz', 'w:gz') as tar:
        for pth in KOBOROOT_DIR.rglob('*'):
            arcname = str(pth).replace(str(KOBOROOT_DIR), '')
            if '.DS_Store' in arcname:
                continue

            tar.add(pth, arcname=arcname)

    # Create dist/VERSION
    with open(dist_path / 'VERSION', 'w') as fp:
        fp.write(version)

    print('Đã tạo file dist/KoboRoot.tgz thành công!')


def main():
    if not os.environ['LRELEASE']:
        print('Chưa cấu hình LRELEASE trong file .env')
        return

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--build', type=str, default='dev', choices=['release', 'dev'])
    parser.add_argument('--version', type=str, help='Version in YYYYMMDD format')
    args = parser.parse_args()

    build = args.build
    version = args.version or date.today().strftime('%Y%m%d')
    if not re.match(r'\d{8}', version):
        print('Lỗi: Version phải đúng format "YYYYMMDD"')
        return

    if build != 'release':
        version += '-' + build

    print(f'=== Phiên bản: {version} ===')

    # Start building
    combine_translations(version)
    copy_fonts()
    generate_tgz(version)

    print('Đã build thành công!')


if __name__ == '__main__':
    main()
