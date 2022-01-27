import factory
import pytest
from django.contrib.auth.models import User
from faker import Faker
from profile.models import Profile
from tests.test_book.fixtures import BookFactory, UserFactory

faker = Faker()


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    follows = factory.SubFactory(UserFactory)
    favorites = factory.SubFactory(BookFactory)
    bio = factory.Faker('text')
    image = factory.Faker('image_url')
