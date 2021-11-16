import pytest


@pytest.fixture
def new_category(db, category_factory):
    category = category_factory.create()
    return category


@pytest.fixture
def new_author(db, author_factory):
    author = author_factory.create()
    return author


@pytest.fixture
def new_book(db, book_factory):
    book = book_factory.create()
    return book


@pytest.fixture
def new_comment(db, comment_factory):
    comment = comment_factory.create()
    return comment


@pytest.fixture
def new_user(db, user_factory):
    user = user_factory.create()
    return user
