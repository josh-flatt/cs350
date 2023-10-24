"""
URL configuration for BridgeOut project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
import helloapp.views_classes as vc
import helloapp.views_functions as vf
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', vf.helloView, name="hello_view"),

    
    path('user/home',            vc.UserHomeView.as_view(),    name='user_home'),
    path('user/',                vc.UserListView.as_view(),    name='user_list'),
    path('user/<int:pk>',        vc.UserDetailView.as_view(),  name='user_detail'),
    path('user/add',             vc.UserAddView.as_view(),  name='user_add'),
    path('user/<int:pk>/delete', vc.UserDeleteView.as_view(),  name='user_delete'),

    path('profile/home',            vc.ProfileHomeView.as_view(),    name='profile_home'),
    path('profile/',                vc.ProfileListView.as_view(),    name='profile_list'),
    path('profile/<int:pk>',        vc.ProfileDetailView.as_view(),  name='profile_detail'),
    path('profile/<int:pk>/',        vc.ProfileUpdateView.as_view(),  name='profile_edit'),
    
]
