import factory
import pytest
from faker import Faker
from book.controllers import category_controller as category
from book.controllers import language_controller as language
from book.controllers import author_controller as author
from book.controllers import book_controller as book
from book.controllers import comment_controller as comment
from book.models import Category, Author, Book, Comment, Language
from tests.test_profile.fixtures import ProfileFactory

faker = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    slug = factory.Faker('slug', value=name)


class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Language

    name = factory.Faker('word')
    slug = factory.Faker('slug', value=name)


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker('word')
    bio = factory.Faker('text')
    slug = factory.Faker('slug', value=name)


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(AuthorFactory)
    language = factory.SubFactory(LanguageFactory)
    name = factory.Faker('word')
    # image = factory.Faker('image_url')
    price = factory.Faker('random_int')
    stock = factory.Faker('random_int')
    available = factory.Faker('boolean')
    description = factory.Faker('text')
    slug = factory.Faker('slug', value=name)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    book = factory.SubFactory(BookFactory)
    profile = factory.SubFactory(ProfileFactory)
    body = factory.Faker('text')


@pytest.fixture
def category_controller(db):
    return category


@pytest.fixture
def language_controller(db):
    return language


@pytest.fixture
def author_controller(db):
    return author


@pytest.fixture
def book_controller(db):
    return book


@pytest.fixture
def comment_controller(db):
    return comment
