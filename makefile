build:
	docker buildx build --load -t kobo-tieng-viet:latest .

deploy:
	docker compose -f docker-compose.yml up

APP_VERSION ?= latest
GH_OWNER    ?= username
GH_REPO     ?= kobo-tieng-viet

deploy-prod:
	@echo "➡️ Deploying image: ghcr.io/$(GH_OWNER)/$(GH_REPO):$(APP_VERSION)"
	@GH_OWNER=$(GH_OWNER) GH_REPO=$(GH_REPO) APP_VERSION=$(APP_VERSION) \
	docker compose -f docker-compose-prod.yml up
