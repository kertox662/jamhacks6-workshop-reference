FROM python:alpine

COPY rest_server /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python3", "main.py" ]