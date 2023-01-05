FROM python:3.8.6
RUN python -m pip install --upgrade pip

RUN apt -qq update && apt -qq install -y git wget pv jq wget python3-dev ffmpeg mediainfo
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8080

CMD ["python", "bot.py" , "--bind", "0.0.0.0:8080"]
