python -m venv virt

source virt/Scripts/activate

pip install django

*pip install mysql

pip install mysql-connector
pip install mysql-connector-python

django-admin startproject crm

cd crm

python manage.py startapp website

...

python manage.py migrate


python manage.py makemigrations