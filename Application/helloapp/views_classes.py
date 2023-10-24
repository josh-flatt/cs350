from django.shortcuts import render
from django.views import View
from .models import AppUser, Profile, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
import helloapp.views_functions as vf
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, RedirectView

class UserHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return ''
        return f'{vf.get_appuser(self.request.user).pk}'
    
class ProfileHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return ''
        return f'{vf.get_profile(vf.get_appuser(self.request.user)).pk}'
    
class ProfileListView(ListView):
    template_name = 'profile/list.html'
    model = Profile
    context_object_name = 'profilelist'
    
class ProfileAddView(LoginRequiredMixin, CreateView):
    template_name = "profile/add.html"
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        form.instance.appuser = vf.get_appuser(self.request.user)
        return super().form_valid(form)
    
class ProfileDetailView(DetailView):
    template_name = 'profile/detail.html'
    model = Profile
    context_object_name = 'profiledetail'

class ProfileUpdateView(UpdateView):
    template_name = "profile/edit.html"
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('profile_list')

class UserListView(ListView):
    template_name = 'user/list.html'
    model = AppUser
    context_object_name = 'userlist'

class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'user/detail.html'
    model = AppUser
    context_object_name = 'userdetail'

class UserAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_add.html'

class UserUpdateView(UpdateView):
    template_name = "user/edit.html"
    model = AppUser
    fields = '__all__'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('user_list')