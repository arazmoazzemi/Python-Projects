# Managepy cheats

* __Create virtual enviroment__

```bash=
sudo apt install python3-pip virtualenv -y
mkdir django
cd django
virtualenv -p python3 env
sourec env/bin/activate
---

<details>
# Diactive env
deactivate
</details>
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

- *Goto /config/settings.py file and add (Class), created app name(blog) on INSTALLED-APPS setcion:*
*class BlogConfig(AppConfig):*

*default_auto_field = 'django.db.models.BigAutoField'*    
*name = 'blog'*

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

- *Example, Change admin URL patterns:*
  
Goto /config/urls.py

*http://127.0.0.1:8000/admin/*
to
*http://127.0.0.1:8000/dashboard/*

```
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Chanege to:

urlpatterns = [
    path('dashboard/', admin.site.urls),
]

```


- *Create first view and add on urls section (/config/urls.py) > views.py*

```
# views.py

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World!")


```

- *Create first view and add on urls section (/config/urls.py) > urls.py*


```

from django.contrib import admin
from django.urls import path
from blog.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
]

```

- *Seperate urls with json*

*Goto blog foloder and create a (urls.py) file:*

```
# \blog\urls.py

from django.urls import path
from .views import home

urlpatterns =[

    path('', home)

]


```

*Prevent from hardcoding define app_name and name on blog urls.py*

```
from django.urls import path
from .views import home

app_name = "blog"
urlpatterns =[
    path('', home, name="home")
]

```
*Goto main urls.py and add incluede path*

```
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]


# Example or change blog url address:
# view === >  http://127.0.0.1:8000/blog

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog', include('blog.urls'))
]


```

- *return api to jason:*

```
### views.py ###

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
    return HttpResponse("Hello World!")

def api(request):
    return JsonResponse({"title": "Hello World!"})


### urls.py###

from django.urls import path
from .views import home, api

app_name = "blog"
urlpatterns =[
    path('', home, name="home"),
    path('api', api, name="api"),
]


### multiple artcles example ### views.py:

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
    return HttpResponse("Hello World!")

def api(request):
    data = {
        "1": {
            "title": "Article one",
            "id": 20,
            "slug": "First Article"
        },
        "2": {
            "title": "Article two",
            "id": 21,
            "slug": "Second Article"
        },
        "3": {
            "title": "Article three",
            "id": 22,
            "slug": "Third Article"
        },

    }
    return JsonResponse(data)


```

- *Render Template*

```
### create template folder at subdet of blog folder === > mkdri /blog/templates ###
### Goto template folder and create home.html ###
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home Page</title>
</head>
<body>
<p>This is home page</p>
</body>
</html>

### Goto blog>views.py and call html file with render ###

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request,"home.html")


```

Example: 
- *use context:*

```
### views.py ###
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def home(request):
    context = {
        "username": "Araz",
        "age": 22,
        "job": "IT Manager"
    }
    return render(request,"home.html", context)


### home.html ###

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home Page</title>
</head>
<body>
<p>username: {{ username}}</p>
<p>age: {{ age}}</p>
<p>job: {{ job}}</p>
</body>
</html>


```









