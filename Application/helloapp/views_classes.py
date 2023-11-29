from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404 #, render
from django.urls import reverse_lazy
# from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, RedirectView

from .forms import ProfilePictureForm
from .models import AppUser, Profile, User, Experience, Education, Skill, Post, Follow
import helloapp.views_functions as vf
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

# Feed Views

class FeedView(LoginRequiredMixin, ListView):
    template_name = 'feed.html'  # Replace with your template path
    context_object_name = 'feed'
    paginate_by = 20  # Set the number of posts to display per page

    def get_queryset(self):
        profile = Profile.get_me(AppUser.get_me(self.request.user))
        following_profiles = Follow.objects.filter(follower=profile).values_list('following', flat=True)
        feed = Post.objects.filter(profile__in=following_profiles).order_by('-timestamp')
        return feed

# Follow Views

class FollowAddView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        profile_to_follow_id = self.kwargs['pk']
        profile_to_follow = get_object_or_404(Profile, id=profile_to_follow_id)
        follower = Profile.get_me(AppUser.get_me(self.request.user))

        follow, created = Follow.objects.get_or_create(follower=follower, following=profile_to_follow)
        # We can use success and fail url logic to route failed adds later
        return reverse_lazy('profile_list')
        
class FollowDeleteView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        profile_to_unfollow_id = self.kwargs['pk']
        profile_to_unfollow = get_object_or_404(Profile, id=profile_to_unfollow_id)
        follower = Profile.get_me(AppUser.get_me(self.request.user))

        follow = Follow.objects.get(follower=follower, following=profile_to_unfollow)
        follow.delete()

        return reverse_lazy('profile_list')

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
    fields = ('firstName', 'lastName', 'birthDate', 'location', 'email')
    
    success_url = reverse_lazy('profile_home')

class ProfilePictureUpdateView(vf.IsUserRecordMixin, UpdateView):
    model = Profile
    form_class = ProfilePictureForm
    template_name = 'profile/addprofilepic.html'
    success_url = reverse_lazy('profile_home')

# Experience Views

class ExperienceAddView(LoginRequiredMixin, CreateView):
    template_name = "experience/add.html"
    model = Experience
    success_url = reverse_lazy('profile_home')

    def form_valid(self, form):
        form.instance.profile = vf.get_profile(self.request.user.appuser)
        return super().form_valid(form)
    
class ExperienceDeleteView(vf.IsUserProfileFromExperienceMixin, DeleteView):
    model = Experience
    template_name = 'experience/delete.html'
    success_url = reverse_lazy('profile_home')

class ExperienceUpdateView(vf.IsUserProfileFromExperienceMixin, UpdateView):
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
    
class EducationDeleteView(vf.IsUserProfileFromEducationMixin, DeleteView):
    model = Education
    template_name = 'education/delete.html'
    success_url = reverse_lazy('profile_home')

class EducationUpdateView(vf.IsUserProfileFromEducationMixin, UpdateView):
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
    
class SkillDeleteView(vf.IsUserProfileFromSkillMixin, DeleteView):
    model = Skill
    template_name = 'skill/delete.html'
    success_url = reverse_lazy('profile_home')

class SkillUpdateView(vf.IsUserProfileFromSkillMixin, UpdateView):
    template_name = "skill/edit.html"
    model = Skill
    fields = '__all__'
    success_url = reverse_lazy('profile_home')

# Post Views

class PostListView(vf.IsUserProfileMixin, DetailView):
    template_name = 'profile/postlist.html'
    model = Profile
    context_object_name = 'postlist'

class PostAddView(LoginRequiredMixin, CreateView):
    template_name = "post/add.html"
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('profile_home')

    def form_valid(self, form):
        form.instance.profile = vf.get_profile(self.request.user.appuser)
        return super().form_valid(form)
    
class PostDeleteView(vf.IsUserPostMixin, DeleteView):
    model = Post
    template_name = 'post/delete.html'
    success_url = reverse_lazy('profile_home')

class PostUpdateView(vf.IsUserPostMixin, UpdateView):
    template_name = "post/edit.html"
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('profile_home')