import factory
import pytest
from faker import Factory
from faker import Faker
from django.contrib.auth.models import User
from book.controller import category_controller as category
from book.controller import author_controller as author
from book.controller import book_controller as book
from book.controller import comment_controller as comment
from book.controller import user_controller as user

from book.models import Category, Author, Book, Comment

faker = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    slug = factory.Faker('slug')


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker('word')
    slug = factory.Faker('slug')
    bio = factory.Faker('text')


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    categories = factory.SubFactory(CategoryFactory)
    authors = factory.SubFactory(AuthorFactory)
    name = factory.Faker('word')
    slug = factory.Faker('slug')
    price = factory.Faker('random_int')
    stock = factory.Faker('random_int')
    available = factory.Faker('boolean')
    description = factory.Faker('text')
    language = factory.Faker('word')
    image = factory.Faker('image_url')


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = factory.Faker('password')


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    books = factory.SubFactory(BookFactory)
    users = factory.SubFactory(UserFactory)
    comment = factory.Faker('text')
    rate = factory.Faker('random_int')


@pytest.fixture
def category_controller(db):
    return category


@pytest.fixture
def author_controller(db):
    return author


@pytest.fixture
def book_controller(db):
    return book


@pytest.fixture
def comment_controller(db):
    return comment


@pytest.fixture
def user_controller(db):
    return user
