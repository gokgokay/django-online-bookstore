import pytest


@pytest.fixture
def category(db, category_factory):
    return category_factory.create()


@pytest.fixture
def author(db, author_factory):
    return author_factory.create()


@pytest.fixture
def book(db, book_factory):
    return book_factory.create()


@pytest.fixture
def comment(db, comment_factory):
    return comment_factory.create()


@pytest.fixture
def user(db, user_factory):
    return user_factory.create()
