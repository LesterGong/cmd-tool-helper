FROM python:3.11-slim

ENV http_proxy "http://127.0.0.1:7890"
ENV https_proxy "http://127.0.0.1:7890"

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

COPY ./*.py /app/
COPY ./prompt /app/prompt
COPY ./templates /app/templates

CMD ["python", "app.py"]
