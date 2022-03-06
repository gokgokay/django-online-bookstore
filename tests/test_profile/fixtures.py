import factory
from django.contrib.auth.models import User
from faker import Faker
from profile.models import Profile

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = factory.Faker('password')
    first_name = factory.Faker('name')
    last_name = factory.Faker('name')
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
