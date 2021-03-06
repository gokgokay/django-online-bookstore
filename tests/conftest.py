import pytest
from faker import Faker
from pytest_factoryboy import register
from django.test.client import Client
from tests.test_profile.fixtures import ProfileFactory, UserFactory
from rest_framework.test import APIClient
from tests.test_book.fixtures import AuthorFactory, BookFactory, CategoryFactory, CommentFactory, LanguageFactory


register(CategoryFactory)
register(LanguageFactory)
register(AuthorFactory)
register(BookFactory)
register(CommentFactory)
register(UserFactory)
register(ProfileFactory)


@pytest.fixture
def faker():
    faker = Faker()
    return faker


@pytest.fixture
def user(db, django_user_model, django_username_field, faker):
    UserModel = django_user_model
    username_field = django_username_field

    try:
        user = UserModel._default_manager.get(**{username_field: faker.name()})
    except UserModel.DoesNotExist:
        user = UserModel._default_manager.create_user(
            faker.name(), faker.password())
    return user


@pytest.fixture
def admin_user(db, django_user_model, django_username_field, faker):
    user_model = django_user_model
    username_field = django_username_field

    try:
        user = user_model._default_manager.get(**{username_field: faker.name()})
    except user_model.DoesNotExist:
        user = user_model._default_manager.create_superuser(
            faker.name(), faker.password(), faker.email())
    return user


@pytest.fixture
def admin_client(db, admin_user):
    client = Client().force_login(admin_user)
    return client


@pytest.fixture
def user_client(db, user):
    client = Client().force_login(user)
    return client


@pytest.fixture
def api_client():
    return APIClient()
