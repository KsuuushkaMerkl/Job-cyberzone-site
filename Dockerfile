FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN mkdir static

RUN pip install poetry && poetry config virtualenvs.create false

RUN poetry install --no-interaction

CMD uvicorn fastAPI:app --host 0.0.0.0 --port 8000 --reload