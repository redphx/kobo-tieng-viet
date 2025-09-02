FROM python:3.13-slim AS qttools5-and-uv-install

RUN apt-get update && apt-get install -y --no-install-recommends \
        curl qttools5-dev-tools

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"
RUN uv self update

FROM qttools5-and-uv-install AS builder
RUN apt-get purge -y --auto-remove curl \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY pyproject.toml .
RUN uv venv && uv sync
COPY . .

# chương trình chính cố định
ENTRYPOINT ["uv", "run", "python", "build.py"]

# tham số mặc định (có thể override bởi docker-compose.yml hoặc docker run)
CMD ["--build", "dev", "--version", "20250902", "--fonts", "./fonts", "--name", "20250902-dev"]
