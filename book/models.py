from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from faker.utils.text import slugify
from core.models import TimeBaseModel

LANGUAGE_CHOICES = (
    ('turkish', 'Turkish'),
    ('english', 'English'),
    ('german', 'German'),
    ('chinese', 'Chinese'),
    ('arabic', 'Arabic'),
)


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
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, db_index=True)
    image = models.ImageField(blank=True, upload_to='uploads', default='default-book-image.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=10)
    available = models.BooleanField(default=True)
    description = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=250)
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
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)

    class Meta:
        ordering = ('user',)
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.body
