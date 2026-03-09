FROM python:3.10.12
WORKDIR /usr/app

COPY requirements.txt /usr/app
RUN pip install --no-cache-dir -r requirements.txt

COPY porrasite/ .
COPY entrypoint.sh /usr/app/entrypoint.sh
RUN chmod +x /usr/app/entrypoint.sh

EXPOSE 8000

CMD ["sh", "/usr/app/entrypoint.sh"]
