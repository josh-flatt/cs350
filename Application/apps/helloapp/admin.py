from django.contrib import admin
from .models import AppUser, UserGroup, UserConnection, UserGroupConnection, Experience, Education, Skill, Post, Company, Message

admin.site.register(AppUser)
admin.site.register(UserGroup)
admin.site.register(UserConnection)
admin.site.register(UserGroupConnection)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Post)
admin.site.register(Company)
admin.site.register(Message)