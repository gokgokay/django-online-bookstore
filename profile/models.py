from django.contrib.auth.models import User
from django.db import models

from book.models import Book
from core.models import TimeBaseModel


class Profile(TimeBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(User, related_name='followed_by', symmetrical=False)
    favorites = models.ManyToManyField(Book, related_name='favorited_by')
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profiles/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.user.username

    def follow(self, profile):
        self.follows.add(profile)

    def unfollow(self, profile):
        self.follows.remove(profile)

    def is_following(self, profile):
        return self.follows.filter(id=profile.id).exists()

    def is_followed_by(self, profile):
        return self.followed_by.filter(id=profile.id).exists()

    def favorite(self, book):
        self.favorites.add(book)

    def unfavorite(self, book):
        self.favorites.remove(book)

    def has_favorited(self, book):
        return self.favorites.filter(id=book.id).exists()
