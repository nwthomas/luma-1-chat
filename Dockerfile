FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install .

EXPOSE 3200

CMD ["python3", "main.py"]