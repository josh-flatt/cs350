from django.contrib import admin

from .models import AppUser, Experience, Education, Skill, Post

admin.site.register(AppUser)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Post)