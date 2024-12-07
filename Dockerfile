FROM python:3.12.8-alpine3.20

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
ENV POETRY_HOME=/opt/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}

WORKDIR /usr/src/app

RUN apk add --update --no-cache \
  gcc \
  libc-dev \
  libffi-dev \
  openssl-dev \
  bash \
  git \
  libtool \
  m4 \
  g++ \
  autoconf \
  automake \
  build-base \
  postgresql-dev

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.in-project true

ADD src ./
RUN poetry install


RUN chmod +x ./entrypoint.sh

