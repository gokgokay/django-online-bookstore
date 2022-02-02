from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from profile.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance, created, **kwargs):
    if created and instance:
        Token.objects.create(user=instance)
