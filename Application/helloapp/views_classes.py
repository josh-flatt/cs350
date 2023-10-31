from django.shortcuts import render
from django.views import View
from .models import AppUser, Profile, User, Experience, Education, Skill
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
import helloapp.views_functions as vf
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, RedirectView

# User Views

class UserHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return ''
        return f'{vf.get_appuser(self.request.user).pk}'
    
class UserListView(ListView):
    template_name = 'user/list.html'
    model = AppUser
    context_object_name = 'userlist'

class UserDetailView(vf.IsUserRecordMixin, DetailView):
    template_name = 'user/detail.html'
    model = AppUser
    context_object_name = 'userdetail'

class UserAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_add.html'

class UserUpdateView(vf.IsUserRecordMixin, UpdateView):
    template_name = "user/edit.html"
    model = AppUser
    fields = '__all__'
    success_url = reverse_lazy('profile_list')

class UserDeleteView(vf.IsUserRecordMixin, DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('profile_list')

# Profile Views

class ProfileHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return ''
        return f'{vf.get_profile(vf.get_appuser(self.request.user)).pk}'
    
class ProfileListView(ListView):
    template_name = 'profile/list.html'
    model = Profile
    context_object_name = 'profilelist'
    
class ProfileDetailView(DetailView):
    template_name = 'profile/detail.html'
    model = Profile
    context_object_name = 'profiledetail'

class ProfileUpdateView(vf.IsUserRecordMixin, UpdateView):
    template_name = "profile/edit.html"
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('profile_home')

# Experience Views

class ExperienceAddView(LoginRequiredMixin, CreateView):
    template_name = "experience/add.html"
    model = Experience
    fields = '__all__'
    success_url = reverse_lazy('profile_home')

    def form_valid(self, form):
        form.instance.profile = vf.get_profile(self.request.user.appuser)
        return super().form_valid(form)
    
class ExperienceDeleteView(vf.IsUserProfileMixin, DeleteView):
    model = Experience
    template_name = 'experience/delete.html'
    success_url = reverse_lazy('profile_home')

class ExperienceUpdateView(vf.IsUserProfileMixin, UpdateView):
    template_name = "experience/edit.html"
    model = Experience
    fields = '__all__'
    success_url = reverse_lazy('profile_home')

# Education Views

class EducationAddView(LoginRequiredMixin, CreateView):
    template_name = "education/add.html"
    model = Education
    fields = '__all__'
    success_url = reverse_lazy('profile_home')

    def form_valid(self, form):
        form.instance.profile = vf.get_profile(self.request.user.appuser)
        return super().form_valid(form)
    
class EducationDeleteView(vf.IsUserProfileMixin, DeleteView):
    model = Education
    template_name = 'education/delete.html'
    success_url = reverse_lazy('profile_home')

class EducationUpdateView(vf.IsUserProfileMixin, UpdateView):
    template_name = "education/edit.html"
    model = Education
    fields = '__all__'
    success_url = reverse_lazy('profile_home')

# Skill Views

class SkillAddView(LoginRequiredMixin, CreateView):
    template_name = "skill/add.html"
    model = Skill
    fields = '__all__'
    success_url = reverse_lazy('profile_home')

    def form_valid(self, form):
        form.instance.profile = vf.get_profile(self.request.user.appuser)
        return super().form_valid(form)
    
class SkillDeleteView(vf.IsUserProfileMixin, DeleteView):
    model = Skill
    template_name = 'skill/delete.html'
    success_url = reverse_lazy('profile_home')

class SkillUpdateView(vf.IsUserProfileMixin, UpdateView):
    template_name = "skill/edit.html"
    model = Skill
    fields = '__all__'
    success_url = reverse_lazy('profile_home')