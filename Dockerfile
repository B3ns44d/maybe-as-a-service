FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY main.py .
COPY responses.json .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]