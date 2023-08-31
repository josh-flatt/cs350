# Milestone 1 - Code 

Create a simple app that runs on the server.

It does not do anything interesting other than show a hard-coded web page.


## What I did 

Install development tools

    Setup Python 3.11

    Install Django (pip install django)

    Create the Git Repo for Project and Documents

    Install Visual Studio Code and setup Github connection

Create a Django app 

    mkdir Application/BridgeOut
    
    cd Application/Bridgeout

    python -m django startproject BridgeOut .
    
    cd ..

    mkdir apps
    
    cd apps

    python manage.py startapp helloapp

config/settings.py

    ALLOWED_HOSTS = [
    "*",
    ]

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        # Styling
        "crispy_forms",
        "crispy_bootstrap4",
        # Apps
        "apps.helloapp",
    ]

apps/helloapp/views_functions.py

    def helloView(request):
        return render(request, "helloView.html")

BridgeOut/urls.py

    from django.urls import path, include
    from django.views.generic import RedirectView

    urlpatterns = [
        path("", RedirectView.as_view(url="helloapp/")),
        path("admin/", admin.site.urls),
        path("helloapp/", include("apps.helloapp.urls")),
    ]

apps/helloapp/urls.py

    from django.urls import path
    import apps.helloapp.views_classes as vc
    import apps.helloapp.views_functions as vf

    urlpatterns = [
        path("", vf.helloView, name="hello_view"),
    ]

Run Server

    python manage.py runserver


## What I will do

Setup Visual Studio to run the code in the debugger.

Build a view with the defined URL, View, Template design pattern.

Display markdown text from a document files that read.


## Concerns and Challenges

So far, so good...
