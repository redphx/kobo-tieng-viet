IMAGE_NAME ?= kobo-tieng-viet
APP_VERSION ?= latest
# gõ: make build - để build docker image ở local
build:
	docker buildx build --load -t $(IMAGE_NAME):$(APP_VERSION) .

# gõ: make build-tgz -để build .tgz file ở local, 
# thư mục app/dist sẽ mount với ./dist khi chạy lệnh trong thư mục dự án
# cấu hình mặc định được thể hiện trong file docker-compose.yml
# các thư mục ./dist ./KoboRoot ./fonts, phải có sẵn trước khi chạy lệnh này
# nếu muốn mount thư mục khác, cầu hình lại trong file .env
IMAGE_NAME ?= kobo-tieng-viet
APP_VERSION ?= latest
build-tgz:
	@IMAGE_NAME=$(IMAGE_NAME) APP_VERSION=$(APP_VERSION) \
	docker compose -f docker-compose.yml up

APP_VERSION ?= latest
GH_OWNER    ?= username # cấu hình github username
GH_REPO     ?= kobo-tieng-viet

GREEN=\033[32m
RESET=\033[0m

# gõ: make build-tgz-prod - để build .tgz file từ publish image
# yêu cầu: github actions: docker-publish build và publish image thành công
# cấu hình mặc định được thể hiện trong file docker-compose-prod.yml
# các thư mục ./dist ./KoboRoot ./fonts, phải có sẵn trước khi chạy lệnh này
# nếu muốn mount thư mục khác, cầu hình lại trong file .env
build-tgz-prod:
	@echo "➡️ Deploying ghcr.io/$(GH_OWNER)/$(GH_REPO):$(APP_VERSION)"
	@APP_VERSION=$(APP_VERSION) GH_OWNER=$(GH_OWNER) GH_REPO=$(GH_REPO) \
	docker compose -f docker-compose-prod.yml up
	@mkdir -p ./savedist
	@CID=$$(docker compose -f docker-compose-prod.yml ps -a -q builder | cut -c1-12) && \
	echo "➡️ Copying /app/dist from containerid ${GREEN}$$CID${RESET} to ./savedist" && \
	docker cp $$CID:/app/dist ./savedist
