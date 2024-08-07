FROM python:3.12-slim

LABEL authors="Evgen_Bedtytskykh"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV PORT=5000

CMD ["sh", "-c", "python app.py --port $PORT"]
