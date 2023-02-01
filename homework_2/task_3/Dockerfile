FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install redis

CMD ["python", "worker.py"]