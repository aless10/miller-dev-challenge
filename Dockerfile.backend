FROM python:3.11

COPY ./pyproject.toml ./poetry.lock* /home/

RUN pip install poetry

WORKDIR /home/

# Just for build, overwritten by compose in development setup
COPY app/ app/
COPY scripts/ scripts/

RUN poetry install --no-root

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

EXPOSE 8000
