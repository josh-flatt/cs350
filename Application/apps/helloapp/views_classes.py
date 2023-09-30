from django.shortcuts import render
from django.views import View
from .models import AppUser
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

class UserListView(ListView):
    template_name = 'user/list.html'
    model = AppUser
    context_object_name = 'users'


class UserDetailView(DetailView):
    template_name = 'user/detail.html'
    model = AppUser
    context_object_name = 'user'


class UserCreateView(CreateView):
    template_name = "user/add.html"
    model = AppUser
    fields = ['userName', 'firstName', 'lastName', 'email', 'birthDate', 'location', 'profilePicture']
    success_url = reverse_lazy('user_list')


class UserUpdateView(UpdateView):
    template_name = "user/edit.html"
    model = AppUser
    fields = ['userName', 'firstName', 'lastName', 'email', 'birthDate', 'location', 'profilePicture']


class UserDeleteView(DeleteView):
    model = AppUser
    template_name = 'user/delete.html'
    success_url = reverse_lazy('user_list')