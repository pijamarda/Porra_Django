FROM python:3.10.12
WORKDIR /usr/app

COPY requirements.txt /usr/app
RUN pip install --no-cache-dir -r requirements.txt

COPY porrasite/ .

EXPOSE 8000


