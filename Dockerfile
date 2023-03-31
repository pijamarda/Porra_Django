FROM python:3.8.16
WORKDIR /home/fgimenez/data/proyectos/django/porra/porrasite

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY porrasite/ .

#CMD [ "ls"]
CMD [ "python", "./manage.py", "runserver","0.0.0.0:8000"]
