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

# gõ: make build-tgz-dev -để build .tgz file ở local, 
# cấu hình runtime mặc định được ghi trong file docker-compose.dev.yml
# các thư mục muốn mount từ host như ./dist ./fonts, phải có sẵn trước khi chạy lệnh này
# nếu cần mount thư mục khác, cấu hình lại trong file .env và docker-compose.dev.yml
IMAGE_NAME ?= kobo-tieng-viet
APP_VERSION ?= latest
build-tgz-dev:
	@IMAGE_NAME=$(IMAGE_NAME) APP_VERSION=$(APP_VERSION) \
	docker compose -f docker-compose.yml up

APP_VERSION ?= latest
GH_OWNER    ?= username # cấu hình github username
GH_REPO     ?= kobo-tieng-viet

GREEN=\033[32m
RESET=\033[0m

# gõ: make build-tgz-prod - để build .tgz file từ publish image
# yêu cầu: github actions: docker-publish build và publish image thành công
# cấu hình runtime mặc định được ghi trong file docker-compose.prod.yml
# các thư mục muốn mount từ host như ./dist ./fonts, phải có sẵn trước khi chạy lệnh này
# nếu cần mount thư mục khác, cấu hình lại trong file .env và docker-compose.prod.yml
build-tgz-prod:
	@echo "➡️ Deploying ghcr.io/$(GH_OWNER)/$(GH_REPO):$(APP_VERSION)"
	@APP_VERSION=$(APP_VERSION) GH_OWNER=$(GH_OWNER) GH_REPO=$(GH_REPO) \
	docker compose -f docker-compose-prod.yml up
	@mkdir -p ./savedist
	@CID=$$(docker compose -f docker-compose-prod.yml ps -a -q builder | cut -c1-12) && \
	echo "➡️ Copying /app/dist from containerid ${GREEN}$$CID${RESET} to ./savedist" && \
	docker cp $$CID:/app/dist ./savedist
