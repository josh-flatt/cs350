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
from django.urls import path #, include
#from django.views.generic import RedirectView

import helloapp.views_classes as vc
import helloapp.views_functions as vf

urlpatterns = [
    path('', vf.helloView, name="hello_view"),

    path('user/',                vc.UserListView.as_view(),    name='user_list'),
    path('user/home',            vc.UserHomeView.as_view(),    name='user_home'),
    path('user/add',             vc.UserAddView.as_view(),  name='user_add'),
    path('user/<int:pk>',        vc.UserDetailView.as_view(),  name='user_detail'),
    path('user/<int:pk>/delete', vc.UserDeleteView.as_view(),  name='user_delete'),

    path('profile/',                vc.ProfileListView.as_view(),    name='profile_list'),
    path('profile/home',            vc.ProfileHomeView.as_view(),    name='profile_home'),
    path('profile/<int:pk>',        vc.ProfileDetailView.as_view(),  name='profile_detail'),
    path('profile/<int:pk>/',        vc.ProfileUpdateView.as_view(),  name='profile_edit'),
    path('profile/<int:pk>/addpic',        vc.ProfilePictureUpdateView.as_view(),  name='profile_pic_edit'),

    path('experience/add',             vc.ExperienceAddView.as_view(),  name='experience_add'),
    path('experience/<int:pk>/delete', vc.ExperienceDeleteView.as_view(),  name='experience_delete'),
    path('experience/<int:pk>/',        vc.ExperienceUpdateView.as_view(),  name='experience_edit'),

    path('education/add',             vc.EducationAddView.as_view(),  name='education_add'),
    path('education/<int:pk>/delete', vc.EducationDeleteView.as_view(),  name='education_delete'),
    path('education/<int:pk>/',        vc.EducationUpdateView.as_view(),  name='education_edit'),

    path('skill/add',             vc.SkillAddView.as_view(),  name='skill_add'),
    path('skill/<int:pk>/delete', vc.SkillDeleteView.as_view(),  name='skill_delete'),
    path('skill/<int:pk>/',        vc.SkillUpdateView.as_view(),  name='skill_edit'),

    path('posts/<int:pk>',             vc.PostListView.as_view(),  name='post_list'),
    path('post/add',             vc.PostAddView.as_view(),  name='post_add'),
    path('post/<int:pk>/delete', vc.PostDeleteView.as_view(),  name='post_delete'),
    path('post/<int:pk>/',        vc.PostUpdateView.as_view(),  name='post_edit'),
    
    path('follow/<int:pk>',        vc.FollowAddView.as_view(),  name='follow_add'),
    path('follow/<int:pk>/delete',        vc.FollowDeleteView.as_view(),  name='follow_add'),

    path('feed/',        vc.FeedView.as_view(),  name='feed'),
]
