FROM python:3.8.6
WORKDIR /app

RUN apt -qq update && apt -qq install -y git ffmpeg
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8080

CMD ["python", "bot.py" , "--bind", "0.0.0.0:8080"]
