import factory
import pytest
from faker import Factory
from django.contrib.auth.models import User
from book.controller import category_controller as category
from book.controller import author_controller as author
from book.controller import book_controller as book
from book.controller import comment_controller as comment
from book.controller import user_controller as user

from book.models import Category, Author, Book, Comment

faker = Factory.create()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = faker.word()
    slug = faker.slug()


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = faker.word()
    slug = faker.slug()
    bio = faker.text()


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    categories = factory.SubFactory(CategoryFactory)
    authors = factory.SubFactory(AuthorFactory)
    name = faker.word()
    slug = faker.slug()
    price = faker.random_int()
    stock = faker.random_int()
    available = faker.boolean()
    description = faker.text()
    language = faker.word()
    image = faker.image_url()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = faker.name()
    password = faker.password()


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    books = factory.SubFactory(BookFactory)
    users = factory.SubFactory(UserFactory)
    comment = faker.text()
    rate = faker.random_int()


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
