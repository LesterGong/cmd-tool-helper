FROM python:3.11-slim

ENV HTTP_PROXY="http://ip:7890/"
ENV HTTPS_PROXY="http://ip:7890/"
ENV NO_PROXY="localhost,127.0.0.1,.example.com"

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./*.py /app/
COPY ./prompt /app/prompt
COPY ./templates /app/templates

EXPOSE 5000

CMD ["python", "app.py"]
