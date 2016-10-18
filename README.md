# Porra Django

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

We need the following APT packages:  
*sudo apt-get install postgresql-server-dev-9.5*  
*sudo apt-get install python3-dev*  
And the following PIP package:  
*sudo pip3 install virtualenv*  

### Install instructions:

1. Clone repo:  
*git clone https://github.com/pijamarda/Porra_Django*

2. Configure PostgreSQL  
*sudo su - postgres*  
*createuser --interactive zeneke*  
*Shall the new role be a superuser? (y/n) y*  
*exit*  
*createdb -U zeneke porra_proyect*  
Now we restore the backup executing the script:  
*cd script*  
*restoredb.sh*  
Change the password of the user created:
*psql porra_proyect*  
*alter user zeneke password 'p0rr4lds';*

3. virtualENV  
Go to the project directory  
*cd Porra_Django*  
create virtualenv:  
*virtualenv-3.5 virtualPorra*  
then activate:  
*source virtualPorra/bin/activate*  

4. Install django packages:  
*pip install -r requirements.txt*    

5. And we test if everything is ok running Django:  
*python porrasite/manage.py runserver*  

6. Modify the settings.py on the project folder, to serve static files in development:  
*vim porrasite/porrasite/settings.py*  
and modify:  
*STATICFILES_DIRS* directive with the current PATH of static files  
*'/home/zeneke/data/proyectos/django/porra_django/porrasite/static/',*   

7. To deactivate the virtial env type:  
*deactivate*  


### Windows install

Not worth it...

## Install WSGI serving pages with NGINX
http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html

