FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential default-libmysqlclient-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip wheel
RUN pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "catalogo.wsgi:application", "--bind", "0.0.0.0:8000"]
