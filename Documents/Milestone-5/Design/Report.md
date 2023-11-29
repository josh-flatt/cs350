# Overview of Milestone 5 Design - Evan Duffield

* What did I do?
    * Created a guide of Design Patterns for the project.
    * Refactored and cleaned up methods/code in the project.
    * Did CSS debugging for homepage.
    * Tested the app's core functions.
    * Turned debugging off, checked for any exposed ports on the server.
* What will I do?  Code for Milestone 6
    * Help finish the last user stories before the end of the semester.
* What challenges do I have?
    * Refactoring a large project without breaking anything.
* Engineering investment
    * I spent about 10 hours on Design for Milestone 5
    * Our team met for 2 hours.
* 5-minute Video Demo
    * [Milestone 5 - Design](https://drive.google.com/file/d/1xyJCLoOpB4V0qoY7gf2wrUoA1YMvhWyY/view?usp=sharing)

## Design Pattern Catalog

See DesignPatterns.md

## Refactoring

Example code from the project before and after changes can be found in the presentation in the same folder.

Overall the project was already fairly factored. variables were declared when reused in most places, and when they weren't such as for the a variable in the dispatch methods in views_functions.py I inlined the variable. I also went through the imported modules and removed anything not in use to improve our performance. I also renamed the IsUserProfileFromExpMixin and IsUserProfileFromEduMixin methods to be more clear and verbose in views_functions.py.

* Removing inline variables
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
Consolidated multiple class imports from the same module into one line.

```
def dispatch(self, request, *args, **kwargs):
        if not self.get_test_func()():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
```
Got rid of "user_test_result" variable that was only used once.

* Renaming Methods
```
class IsUserProfileFromEducationMixin(AccessMixin):
    def test_func(self):
        education = get_object_or_404(Education, pk = self.kwargs["pk"])
        return self.request.user == education.profile.appuser.user
```
Changed Class/Method name from an abbreviated version to a verbose one that follows PEP-8.

## Help with implementation

I helped with implementation this Milestone by testing the application and making modifications for production. This involved:

* Tested the app's major functions, experimented with input limits to assure a crash couldn't occur as a result.
* Changing settings.py to be production ready. The most important part of this was setting DEBUG to False, so attackers cant find out our Django version data by giving a bad url.
* Making sure our web server's HTTP/HTTPS ports were the only open ports. This was done with a traceroute to our digitalocean app, before using the resulting IP to do a port scan.
* Adding css in some rough areas into the html to make things centered and presentable.
```
style="margin:25px; width: 95%; justify-content: center;"
```
An example, the css used to center the card body on the front page.

## AI Prompts

ChatGPT was able to help a lot with refactoring and coming up with large strings to test input on the website. You can see the responses in AI.md, but here are some of the prompts I asked:

* What are some design patterns that can help organize a large Django project?
* What are some examples of design patterns?
* How would you refactor this method?
```
def get_queryset(self):
        profile = Profile.get_me(AppUser.get_me(self.request.user))
        following_profiles = Follow.objects.filter(follower=profile).values_list('following', flat=True)
        feed = Post.objects.filter(profile__in=following_profiles).order_by('-timestamp')
        return feed
```
* What is the standard for storing local modules in a django project?
* What could this method be renamed to make it more maintainable?
```
@property
    def following_profiles(self):
        """
        Get the list of profiles that the current profile is following.
        """
        follow_objects = Follow.objects.filter(follower=self)
        return [follow_object.following for follow_object in follow_objects]
```
* Give me some strings to test input limits on my website.
