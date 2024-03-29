# Porra Django

## New working version running fully on containers

### Prerequisites

You need to have docker installed with:  
- docker compose command

### Instructions

Create a .env file, you can use the file .example.env as an example  
Type:  
```
source .env
```
Now execute  
```
docker compose up --build  
```
Now the web should be reachable on:  
http://localhost:8000  
with at least 2 users

And the admin panel on  
http://localhost:8000/admin  
You can use the credentials defined on the .env file

## OLD VERY OLD INSTRUCTIONS  

## Linux install (instructions for Ubuntu Server 14.04):

### Pre-requisites:

PostgreSQL:  
Check with:  
*psql --version*  
psql (PostgreSQL) 9.5.4

We need to install Postgresql Database from:  
http://www.postgresql.org/download/linux/  
These commands should be enough (for 9.5 version):  
*sudo apt-get install postgresql-9.5*  
If the 9.5 is not in the repository follow instructions here:  
http://www.postgresql.org/download/linux/ubuntu/  
and then repeat the command:  
*sudo apt-get install postgresql-9.5*  

Python3 must be installed in the system, with pip/pip3 commands available:  
https://www.python.org/downloads/  
*sudo apt-get install python3*  
check if pip3 is installed:  
*pip3* (or check for pip-3..)  
if not use  
*sudo apt-get install python3-pip*  

We also need Git installed:  
*apt-get install git*  

We need the following APT packages for the pip installation:  
*sudo apt-get install postgresql-server-dev-9.5*  
*sudo apt-get install python3-dev*  
And the following PIP package:  
*sudo pip3 install virtualenv*  

### Install instructions:

1. Clone repo:  
*git clone https://github.com/pijamarda/Porra_Django*

2. Add user 'zeneke' to the system:  
*sudo adduser zeneke*  

3. Configure PostgreSQL  
*sudo su - postgres*  
*createuser --interactive zeneke*  
*Shall the new role be a superuser? (y/n) y*  
Change the password of the user created:  
*psql*  
*alter user zeneke password 'p0rr4lds';*  
*create database porra_proyect;*  
*grant all privileges on database porra_proyect to zeneke;*   
*\q*  
*exit*  
Now we restore the backup executing the script as the user 'zeneke':  
*su - zeneke*  
*cd ..porra_django/script*    
*restoredb.sh*  

4. virtualENV  
Go to the project directory  
*cd Porra_Django*  
create virtualenv:  
*virtualenv virtualPorra*  
then activate:  
*source virtualPorra/bin/activate*  

5. Install django packages:  
*pip install -r requirements.txt*    

6. And we test if everything is ok running Django:  
*python porrasite/manage.py runserver*  

7. Modify the settings.py on the project folder, to serve static files in development:  
*vim porrasite/porrasite/settings.py*  
and modify:  
*STATICFILES_DIRS* directive with the current PATH of static files  
*'/home/zeneke/data/proyectos/django/porra_django/porrasite/static/',*   

8. To deactivate the virtial env type:  
*deactivate*  


### Windows install

Not worth it...

## Install WSGI serving pages with NGINX
http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html

