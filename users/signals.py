from django.contrib.auth.models import User
from users.models import Profile, ProfileStatus
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_first_status_message(sender, instance, created, **kwargs):
    if created:
        ProfileStatus.objects.create(
            user_profile=instance,
            message=f'{instance.user.username} created successfully')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)