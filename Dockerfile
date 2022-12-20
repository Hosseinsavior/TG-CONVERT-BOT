FROM python:3.8.6
WORKDIR /app

RUN apt -qq update && apt -qq install -y git ffmpeg
COPY . .
ADD . /app
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080

CMD ["python", "bot.py"]