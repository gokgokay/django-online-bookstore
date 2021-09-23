import uuid
from django.db import models
from django.contrib.auth.models import User
from core.models import TimeBaseModel


class Profile(TimeBaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile_img/%Y/%m')

    class Meta:
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username


class ProfileStatus(TimeBaseModel):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Profile Statuses'

    def __str__(self):
        return str(self.user_profile)
