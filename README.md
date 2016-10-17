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

### Install instruccions:

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

3. virtualENV  
Go to the project directory  
*cd Porra_Django*  
create virtualenv:  
*virtualenv-3.4 virtualPorra*  
then activate:  
*source virtualPorra/bin/activate*  

4. Install django packages:  
*pip install django==1.7*  
*pip install psycopg2==2.5.4*  

5. And we test if everything is ok running Django:  
*python python porrasite/manage.py runserver*  

6. To deactivate the virtial env type:  
*deactivate*  


### Windows install

Not worth it...

## Install WSGI serving pages with NGINX
http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html

