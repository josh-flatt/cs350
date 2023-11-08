"""
BridgeOut Project URL Configuration

This configuration provides a guide to mapping URLs to their respective views.
For an in-depth understanding, refer to:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Usage:
- For function views:
    1. Import your view:  from my_app import views
    2. Add the URL to urlpatterns:  path('', views.home, name='home')
    
- For class-based views:
    1. Import your view:  from other_app.views import Home
    2. Add the URL to urlpatterns:  path('', Home.as_view(), name='home')
    
- To include another URL configuration:
    1. Import the required functions: from django.urls import include, path
    2. Include the URL configuration:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", RedirectView.as_view(url="helloapp/")),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', RedirectView.as_view(url='/helloapp/user/home')),
    path("helloapp/", include("helloapp.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)