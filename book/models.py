from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from core.models import TimeBaseModel


class Category(TimeBaseModel):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    @property
    def to_json(self):
        return {
            "id": self.pk,
            "name": self.name,
            "slug": self.slug,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class Author(TimeBaseModel):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    bio = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name

    @property
    def to_json(self):
        return {
            "id": self.pk,
            "name": self.name,
            "slug": self.slug,
            "bio": self.bio,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class Book(TimeBaseModel):
    categories = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    authors = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='books/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=10)
    available = models.BooleanField(default=True)
    description = models.TextField()
    language = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name

    @property
    def to_json(self):
        return {
            "id": self.pk,
            "categories": self.categories,
            "authors": self.authors,
            "name": self.name,
            "slug": self.slug,
            "price": self.price,
            "stock": self.stock,
            "available": self.available,
            "description": self.description,
            "language": self.language,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class Comment(TimeBaseModel):
    books = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    users = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        ordering = ('rate',)
        verbose_name_plural = 'Comments'

    def __str__(self):
        return str(self.rate)

    @property
    def to_json(self):
        return {
            "id": self.pk,
            "books": self.books,
            "profile": self.users,
            "comment": self.comment,
            "rate": self.rate,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
