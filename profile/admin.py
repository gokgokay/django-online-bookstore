from django.contrib import admin
from profile.models import Profile, ProfileStatus


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']


@admin.register(ProfileStatus)
class ProfileStatusAdmin(admin.ModelAdmin):
    list_display = ['message']
