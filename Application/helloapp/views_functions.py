from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import get_object_or_404
from .models import AppUser, Post, Profile, User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

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
        user_test_result = self.get_test_func()()
        if not user_test_result:
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
        user_test_result = self.get_test_func()()
        if not user_test_result:
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