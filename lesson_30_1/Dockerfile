FROM python:3.9-slim

ENV PYTHONPATH="/app/src:${PYTHONPATH}"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY tests/ ./tests/

CMD ["pytest", "tests/", "--alluredir=allure-results"]