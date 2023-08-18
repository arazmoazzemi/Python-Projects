# Managepy cheats

```
sudo apt install python3-pip virtualenv -y
mkdir django
cd django
virtualenv -p python3 env

sourec env/bin/activate

# Diactive env
deactivate

# windows # python.exe -m pip install --upgrade pip

(venv) C:\Users\DevOps\PycharmProjects\myproject>

pip install django

django-admin

# 01:
django-admin startproject config

# Change config folder name
# rename config myproject
mv config myproject

#02 :
cd myproject
python ./manage.py
python ./manage.py migrate


# 03:
python ./manage.py runserver

# 127.0.0.1:8000



python ./managepy createsuperuser


# Create an app
# This method is not recommended fot production projects,
# For production build an app for each project


cd myproject
source /env/bin/activate
python ./managepy startapp blog


```

*Goto /config/settings.py file and add (Class), created app name(blog) on INSTALLED-APPS setcion:*
*class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'*

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'blog.apps.BlogConfig'
]



```













