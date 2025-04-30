FROM python:3.11-slim-buster AS base


WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ app/
COPY model/ model/

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]