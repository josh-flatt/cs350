from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import AppUser, Post, Profile, User, Experience, Education, Skill

# Create your views here.

class IsUserRecordMixin(AccessMixin):
    def test_func(self):
        user = get_object_or_404(User, pk = self.kwargs["pk"])
        return self.request.user == user

    def get_test_func(self):
        """
        Override this method to use a different test_func method.
        """
        return self.test_func

    def dispatch(self, request, *args, **kwargs):
        if not self.get_test_func()():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class IsUserProfileMixin(AccessMixin):
    def test_func(self):
        profile = get_object_or_404(Profile, pk = self.kwargs["pk"])
        return self.request.user == profile.appuser.user

    def get_test_func(self):
        """
        Override this method to use a different test_func method.
        """
        return self.test_func

    def dispatch(self, request, *args, **kwargs):
        if not self.get_test_func()():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    
class IsUserPostMixin(AccessMixin):
    def test_func(self):
        post = get_object_or_404(Post, pk = self.kwargs["pk"])
        return self.request.user == post.profile.appuser.user

    def get_test_func(self):
        """
        Override this method to use a different test_func method.
        """
        return self.test_func

    def dispatch(self, request, *args, **kwargs):
        if not self.get_test_func()():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    
class IsUserProfileFromExperienceMixin(AccessMixin):
    def test_func(self):
        experience = get_object_or_404(Experience, pk = self.kwargs["pk"])
        return self.request.user == experience.profile.appuser.user

    def get_test_func(self):
        """
        Override this method to use a different test_func method.
        """
        return self.test_func

    def dispatch(self, request, *args, **kwargs):
        if not self.get_test_func()():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class IsUserProfileFromEduMixin(AccessMixin):
    def test_func(self):
        education = get_object_or_404(Education, pk = self.kwargs["pk"])
        return self.request.user == education.profile.appuser.user

    def get_test_func(self):
        """
        Override this method to use a different test_func method.
        """
        return self.test_func

    def dispatch(self, request, *args, **kwargs):
        if not self.get_test_func()():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class IsUserProfileFromSkillMixin(AccessMixin):
    def test_func(self):
        skill = get_object_or_404(Skill, pk = self.kwargs["pk"])
        return self.request.user == skill.profile.appuser.user

    def get_test_func(self):
        """
        Override this method to use a different test_func method.
        """
        return self.test_func

    def dispatch(self, request, *args, **kwargs):
        if not self.get_test_func()():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

def helloView(request):
    return render(request, "helloView.html")

def list_posts(appuser):
    return dict(posts=Post.objects.filter(appuser=appuser))

def get_appuser(user):
    return AppUser.objects.get_or_create(user=user)[0]

def get_profile(appuser):
    return Profile.objects.get_or_create(appuser=appuser)[0]