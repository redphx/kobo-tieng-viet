#!/bin/sh
set -e
echo "⏳ Đang chuẩn bị build KoboRoot.tgz..."

uv run python build.py --build $BUILD --version $VERSION --fonts $FONTS_DIR

echo "✅ Hoàn thành tạo file dist/KoboRoot.tgz (phiên bản: $VERSION-$BUILD)"
exit 1