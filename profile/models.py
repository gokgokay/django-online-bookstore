from django.contrib.auth.models import User
from django.db import models
from core.models import TimeBaseModel


class Profile(TimeBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_books = models.ManyToManyField('book.Book', related_name='favorited_by', blank=True)
    follows = models.ManyToManyField('self', related_name='followed_by', blank=True, symmetrical=False)
    bio = models.TextField(blank=True)
    phone = models.CharField(blank=True, max_length=150)
    image = models.ImageField(blank=True, upload_to='uploads', default='default-profile-image.jpg')

    class Meta:
        ordering = ('user',)
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username

    def follow(self, profile):
        self.follows.add(profile)

    def unfollow(self, profile):
        self.follows.remove(profile)

    def is_followed_by(self, profile):
        return self.followed_by.filter(pk=profile.pk).exists()

    def favorite(self, book):
        self.favorite_books.add(book)

    def unfavorite(self, book):
        self.favorite_books.remove(book)

    def has_favorited(self, book):
        return self.favorite_books.filter(id=book.id).exists()
