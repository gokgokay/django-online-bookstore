import factory
from faker import Factory
from django.contrib.auth.models import User
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
