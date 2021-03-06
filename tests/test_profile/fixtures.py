import factory
import pytest
from django.contrib.auth.models import User
from faker import Faker
from profile.models import Profile
from profile.controllers import user_controller as user
from profile.controllers import profile_controller as profile

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('first_name')
    password = factory.Faker('password')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    is_staff = factory.Faker('boolean')
    is_active = factory.Faker('boolean')
    date_joined = factory.Faker('date_time')


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    bio = factory.Faker('word')
    phone = factory.Faker('word')


@pytest.fixture
def user_controller(db):
    return user


@pytest.fixture
def profile_controller(db):
    return profile
