FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app

CMD ["sh", "-c", "sleep 5 && python app/seed.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
