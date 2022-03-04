from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from faker.utils.text import slugify
from core.models import TimeBaseModel
from profile.models import Profile


class Category(TimeBaseModel):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(str(value), allow_unicode=True)
        super().save(*args, **kwargs)


class Language(TimeBaseModel):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(str(value), allow_unicode=True)
        super().save(*args, **kwargs)


class Author(TimeBaseModel):
    name = models.CharField(max_length=250, db_index=True)
    bio = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(str(value), allow_unicode=True)
        super().save(*args, **kwargs)


class Book(TimeBaseModel):
    category = models.ForeignKey('book.Category', related_name='categories', on_delete=models.CASCADE)
    author = models.ForeignKey('book.Author', related_name='authors', on_delete=models.CASCADE)
    language = models.ForeignKey('book.Language', related_name='languages', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, db_index=True)
    image = models.ImageField(blank=True, upload_to='uploads', default='default-book-image.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=10)
    available = models.BooleanField(default=True)
    description = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name', 'language',)
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(str(value), allow_unicode=True)
        super().save(*args, **kwargs)


class Comment(TimeBaseModel):
    book = models.ForeignKey('book.Book', related_name='books', on_delete=models.CASCADE)
    profile = models.ForeignKey('profile.Profile', related_name='users', on_delete=models.CASCADE, default=None)
    body = models.TextField(max_length=1000)

    class Meta:
        ordering = ('profile',)
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.body
