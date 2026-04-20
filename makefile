# install qttools5 and uv
# make env
env:
	@sudo apt-get install -y --no-install-recommends curl qttools5-dev-tools \
	&& curl -fsSL https://astral.sh/uv/install.sh -o ./uv-installer.sh \
	&& . ./uv-installer.sh && rm ./uv-installer.sh \
	&& export PATH="$$HOME/.local/bin/:$$PATH" \
	&& uv self update

install: 
	uv sync

BUILD 		?= dev
VERSION 	?= 20250904
FONTS		?= ./fonts
TGZ_NAME 	?= test

# ghi đè param
# gõ: make run BUILD=release VERSION=20250905 ...
run:
	uv run python build.py --build $(BUILD) --version $(VERSION) --fonts $(FONTS) --name $(TGZ_NAME)

IMAGE_NAME ?= kobo-tieng-viet
APP_VERSION ?= latest
# gõ: make build-image - để build docker image ở local
build-image:
	docker buildx build --load -t $(IMAGE_NAME):$(APP_VERSION) .

# gõ: make build-tgz-dev -để build .tgz file ở local (môi trường docker)
# cấu hình runtime mặc định được ghi trong file docker-compose.dev.yml
# các thư mục muốn mount từ host như ./dist ./fonts, phải có sẵn trước khi chạy lệnh này
# nếu cần mount thư mục khác, cấu hình lại trong file .env và docker-compose.dev.yml
IMAGE_NAME ?= kobo-tieng-viet
APP_VERSION ?= latest
build-tgz-dev:
	@IMAGE_NAME=$(IMAGE_NAME) APP_VERSION=$(APP_VERSION) \
	docker compose -f docker-compose.dev.yml up

# make all được dùng trong build và release flow
BUILD 		:= release
VERSION 	:= $(shell date +%Y%m%d)
FONTS		:= ./fonts
LRELEASE=/usr/bin/lrelease
UV_LINK_MODE=copy
export LRELEASE
export UV_LINK_MODE
all:
	uv run python build.py --build $(BUILD) --version $(VERSION) --fonts $(FONTS)

