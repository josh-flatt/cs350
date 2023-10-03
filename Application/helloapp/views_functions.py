from django.shortcuts import render
from django.views import View
from .models import AppUser
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

# Create your views here.

def helloView(request):
    return render(request, "helloView.html")