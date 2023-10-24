from django.shortcuts import render
from django.views import View
from .models import AppUser, Post, Profile
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

# Create your views here.

def helloView(request):
    return render(request, "helloView.html")

def list_posts(appuser):
    return dict(posts=Post.objects.filter(appuser=appuser))

def get_appuser(user):
    return AppUser.objects.get_or_create(user=user)[0]

def get_profile(appuser):
    return Profile.objects.get_or_create(appuser=appuser)[0]