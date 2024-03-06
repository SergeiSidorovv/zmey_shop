FROM python:3.12.2-slim-bookworm AS build_docker

WORKDIR /zmey_shop
COPY --chown=sergeisidorov801:sergeisidorov801 requirements.txt requirements.txt 
RUN apt-get update \
    && pip install --upgrade pip 

FROM python:3.12.2-slim-bookworm

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBUTECODE=1

WORKDIR /zmey_shop
EXPOSE 8000

RUN adduser --system --group sergeisidorov801

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-client-15 

COPY --chown=sergeisidorov801:sergeisidorov801 --from=build_docker zmey_shop/requirements.txt requirements.txt
COPY --chown=sergeisidorov801:sergeisidorov801 zmey_shop /zmey_shop

RUN --mount=type=cache,target=/root/.cache/pip \ 
    pip install  -r requirements.txt

USER sergeisidorov801