# Build stage
FROM python:3.10-buster AS build

RUN apt-get update

# Install poetry
RUN pip install -U pip poetry

# Set up
RUN mkdir -p /app
WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.in-project true && \
    poetry install --no-dev --no-interaction

# Run stage
FROM python:3.10-slim-buster AS runtime

COPY --from=build /app/.venv /app/.venv
ENV PATH=/app/.venv/bin:$PATH

COPY questions /app/questions
COPY config.ini /app

WORKDIR /app/
EXPOSE 8080

CMD ["uvicorn", "questions.main:app", "--host", "0.0.0.0", "--reload", "--port", "8080"]