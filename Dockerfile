FROM python:3.13-slim

ENV POETRY_VERSION=2.1.2 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/root/.local" \
    PATH="/root/.local/bin:$PATH"

    RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        g++ \
        make \
        cmake \
        curl \
        gnupg2 \
        wget \
        unzip \
        chromium \
        chromium-driver \
        libglib2.0-0 \
        libnss3 \
        libgconf-2-4 \
        libfontconfig1 \
        libx11-6 \
        libxext6 \
        libsm6 \
        libxrender1 \
        libxcomposite1 \
        libxcursor1 \
        libxdamage1 \
        libxi6 \
        libxtst6 \
        libxrandr2 \
        libasound2 \
        libatk1.0-0 \
        libatk-bridge2.0-0 \
        libgtk-3-0 \
        libdbus-glib-1-2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi --no-root

COPY . .

EXPOSE 5000

CMD ["poetry", "run", "python", "main.py"]