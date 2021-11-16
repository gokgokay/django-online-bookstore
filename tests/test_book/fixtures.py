import factory
import pytest

from book.models import Category, Author, Book, Comment


@pytest.fixture
def category_factory(session):
    class CategoryFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = Category

        name = factory.Faker("word")
        slug = factory.Faker("slug")

    return CategoryFactory


