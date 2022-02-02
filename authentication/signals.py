from django.contrib.auth.models import User
from profile.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance:
        Profile.objects.create(user=instance)

