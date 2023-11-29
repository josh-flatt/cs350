# Design Pattern Catalog

After reviewing the project: I decided on these design patterns to choose for the catalog:


* Keep requirements.txt updated. 
  * This is so the team isn't stuck trying to figure out how to get the proper version of a dependency someone adds to the project.
  ```
    black
    django
    django-crispy-forms
    crispy-bootstrap4
    asgiref
    dj-database-url
    gunicorn
    psycopg2-binary
    pytz
    markdown
    requests
    pillow
    sqlparse
    whitenoise
  ```
* Separate local imports from modules.
  * It can be difficult to trace local module use in the project when it is imported in the middle of a large group of Django modules.
  ```
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.shortcuts import get_object_or_404
    from django.urls import reverse_lazy
    from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, RedirectView

    from .forms import ProfilePictureForm
    from .models import AppUser, Profile, User, Experience, Education, Skill, Post, Follow
    import helloapp.views_functions as vf
  ```
* Maintain a Model-View-Controller design pattern using Django's Model-View-Template pattern.
  * I have been on a lot of projects where people wanted to take a Java approach of having one class per file. Since this application is relatively simple, so we wanted to keep as few files as possible. models.py, views_classes.py, vews_functions.py, and the templates all form Django's Model-View-Template, which focuses more on the front-end than a controller.
  
  Model:
  ```
  class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)

    accountCreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'
    
    def get_absolute_url(self):
        return reverse_lazy('user_detail', args=[str(self.id)])
  ```

  View:
  ```
    class UserAddView(CreateView):
        form_class = UserCreationForm
        success_url = reverse_lazy('login')
        template_name = 'registration/account_add.html'

    class UserUpdateView(vf.IsUserRecordMixin, UpdateView):
        template_name = "user/edit.html"
        model = AppUser
        fields = '__all__'
        success_url = reverse_lazy('profile_list')
  ```

  Template:
  ```
    {% extends 'theme.html' %}

    {% block title %}
    Edit Profile
    {% endblock title %}

    {% block content %}
    <html lang="en">

    <head>
        {% load static %}
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BridgeOut - Edit Profile</title>
        <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    </head>

    <body>
  ```

Including those, I have also chosen to have standards for:

* Methods
  * Official Python Style Guide PEP-8: "Function names should be lowercase, with words separated by underscores as necessary to improve readability."
  * Functional Programming: Methods should do one thing and do it well.
  ```
    def test_profile_update_view(self):
        url = reverse('profile_edit', args=[str(self.profile.pk)])
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_experience_add_view(self):
        url = reverse('experience_add')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
  ```
  These methods follow the PEP-8 standard using lowercase whole words with underscores. They also show functional programming by each of the methods focusing on only one operation of the system to test at a time.

* Variables
  * Official Python Style Guide PEP-8: "Variable names follow the same convention as function names."
  * Whole words: single-letter variables shouldn't be used outside of loop contexts.
  ```
    @property
    def following_profiles(self):
        """
        Get the list of profiles that the current profile is following.
        """
        follow_objects = Follow.objects.filter(follower=self)
        return [follow_object.following for follow_object in follow_objects]
    
    @property
    def follower_profiles(self):
        """
        Get the list of profiles that are following the current profile.
        """
        follow_objects = Follow.objects.filter(following=self)
        return [follow_object.follower for follow_object in follow_objects]
  ```
    These methods might not have that many variables, but the ones that they do have follow identical naming conventions as the methods. In the list comprehension on both methods they use a whole variable name to improve readibility, even if its a temporary inline variable.

* Comments
  * Official Python Style Guide PEP-8: "Use inline comments sparingly."
  * Self documenting. Python is meant to be a readable language. Any comments should only be vital information.
  * On larger documents, comments are ok to use to divide a file into sections.
  ```
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
  ```
  Here the inline comment is only reserved for the most complicated part of the method. Above the two classes, a comment is used to mark that the section of the file is reserved for viewing Followings.

* Classes
  * Official Python Style Guide PEP-8: "Class names should normally use the CapWords convention."
  * Classes should inherit as much from the Django superclasses as possible to prevent developers reinventing the wheel.
  ```
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
  ```
    All of these classes both use CapWords for class names and inherit from a Django superclass.