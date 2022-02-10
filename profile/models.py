from django.contrib.auth.models import User
from django.db import models
from book.models import Book
from core.models import TimeBaseModel


class Profile(TimeBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follow = models.ManyToManyField('self', related_name='profile', symmetrical=False)
    favorite = models.ManyToManyField(Book, related_name='profile')
    bio = models.TextField(blank=True)
    phone = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=150)
    country = models.CharField(blank=True, max_length=150)
    image = models.ImageField(blank=True, upload_to='uploads', default='default-profile-image.jpg')

    class Meta:
        ordering = ('user',)
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username

    def follow_user(self, profile):
        self.follow.add(profile)

    def unfollow_user(self, profile):
        self.follow.remove(profile)

    def is_following_user(self, profile):
        return self.follow.filter(id=profile.id).exists()

    def is_followed_by(self, profile):
        return self.profile.follow.filter(id=profile.id).exists()

    def favorite_user(self, book):
        self.favorite.add(book)

    def unfavorite_user(self, book):
        self.favorite.remove(book)

    def has_favorited_user(self, book):
        return self.favorite.filter(id=book.id).exists()
