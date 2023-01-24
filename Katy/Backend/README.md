## Add New App
python manage.py startapp v1
## EX:
python manage.py startapp authorization
## create file .env and next lines
SECRET_KEY='i@((w^#%8l5ebi$7b@*$h)g%05!vk@osqxmxttb41zk#$q_h#k'
REFRESH_TOKEN_SECRET='a@((w^#%8l5ebi$7b@*$h)s%05!wk@osqxmxttb41zk#$q_h#M'
DEBUG = 1
HTTPS = 0
DATABASE_NAME='damian_db'
DATABASE_USER='root'
DATABASE_PASSWORD=''
DATABASE_HOST='localhost'
DATABASE_PORT='3306'
SMTP_HOST='smtp.gmail.com'
EMAIL_HOST='waledmet@gmail.com'
EMAIL_PASSWORD_HOST='123456'
LOG_ENABLE=0
## mysql server Creat DataBase
database name : damian_db
character set : utf8mb4
Collation : utf8mb4_general_ci
## Create Database Migration
python manage.py migrate
## createsuperuser (password 123456)
python manage.py createsuperuser --username admin --email waledmet@gmail.com
## Create Database for app
python manage.py makemigrations app_name
python manage.py migrate app_name
## EX:
python manage.py makemigrations v1
python manage.py migrate v1

## add initial Data to Database
python manage.py initialData

## Add Backend Api (Ex : BasicData in Authorization)
1- Add file for url in urls folder (authorization/urls/basicdata.py)
2- Add file for view in Views folder (authorization/views/basicdata.py)
2- add refrence to url file in main url file (authorization/urls/urls.py)
## Shared Folder
1-general.py  will contain all common functions in the system
2-authentication.py will contain all functions will check Permissions and access
3-utils.py will contain two main functions to create token and regenerate it again 
4-vars.py will contain all variables will need in the system


## Download docker for Redis Channels
1. https://www.docker.com/products/docker-desktop
2. it will be required to download WSL2
3. Restart device 
4. download wsl_update_x64.msi and run it 
5. open CMD write " docker pull redis"
6. open images in docker then run redis
    in optional settings-> ports-> local host-> write " 6379"
https://www.memurai.com/ port =6378
## GPU Commands
1. nvidia-smi    to check cuda version and Persistence Mode
2.  to switch on Persistance Mode sudo nvidia-smi -pm 1 
3.  to switch off Persistance Mode sudo nvidia-smi -pm 0