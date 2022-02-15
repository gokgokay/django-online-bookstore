import factory
import pytest
from faker import Faker
from book.controller import category_controller as category
from book.controller import author_controller as author
from book.controller import book_controller as book
from book.controller import comment_controller as comment
from book.controller import user_controller as user
from book.models import Category, Author, Book, Comment
from tests.test_profile.fixtures import UserFactory

faker = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

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
    name = factory.Faker('word')
    #image = factory.Faker('image_url')
    price = factory.Faker('random_int')
    stock = factory.Faker('random_int')
    available = factory.Faker('boolean')
    description = factory.Faker('text')
    language = factory.Faker('random_choices', elements=['Turkish', 'English', 'German', 'Chinese', 'Arabic'])
    slug = factory.Faker('slug', value=name)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    book = factory.SubFactory(BookFactory)
    user = factory.SubFactory(UserFactory)
    body = factory.Faker('text')


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
