import factory
from django.db.models import signals

from tests.test_book.fixtures import book_controller, language_controller, comment_controller, author_controller, \
    category_controller


def test_get_category(db, category_controller, category_factory, check):
    category = category_factory()
    expected_category = category_controller.get_category(category.id)
    check.equal(category, expected_category)


def test_get_language(db, language_controller, language_factory, check):
    language = language_factory()
    expected_language = language_controller.get_language(language.id)
    check.equal(language, expected_language)


def test_get_author(db, author_controller, author_factory, check):
    author = author_factory()
    expected_author = author_controller.get_author(author.id)
    check.equal(author, expected_author)


def test_get_book(db, book_controller, book_factory, check):
    book = book_factory()
    expected_book = book_controller.get_book(book.id)
    check.equal(book, expected_book)


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_get_comment(db, comment_controller, comment_factory, check):
    comment = comment_factory()
    expected_comment = comment_controller.get_comment(comment.id)
    check.equal(comment, expected_comment)


def test_list_category(db, category_controller, category_factory, check):
    categories = category_factory.create_batch(5)
    expected_categories = category_controller.list_categories_by_filters()
    check.equal(len(categories), len(expected_categories))


def test_list_language(db, language_controller, language_factory, check):
    languages = language_factory.create_batch(5)
    expected_languages = language_controller.list_languages_by_filters()
    check.equal(len(languages), len(expected_languages))


def test_list_author(db, author_controller, author_factory, check):
    authors = author_factory.create_batch(5)
    expected_authors = author_controller.list_authors_by_filters()
    check.equal(len(authors), len(expected_authors))


def test_list_book(db, book_controller, book_factory, check):
    books = book_factory.create_batch(5)
    expected_books = book_controller.list_books_by_filters()
    check.equal(len(books), len(expected_books))


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_list_comment(db, comment_controller, comment_factory, check):
    comments = comment_factory.create_batch(5)
    expected_comments = comment_controller.list_comments_by_filters()
    check.equal(len(comments), len(expected_comments))


def test_list_empty_category(db, category_controller, check):
    expected_category = category_controller.list_categories_by_filters()
    check.equal(0, len(expected_category))


def test_list_empty_language(db, language_controller, check):
    expected_language = language_controller.list_languages_by_filters()
    check.equal(0, len(expected_language))


def test_list_empty_author(db, author_controller, check):
    expected_author = author_controller.list_authors_by_filters()
    check.equal(0, len(expected_author))


def test_list_empty_book(db, book_controller, check):
    expected_book = book_controller.list_books_by_filters()
    check.equal(0, len(expected_book))


def test_list_empty_comment(db, comment_controller, check):
    expected_comment = comment_controller.list_comments_by_filters()
    check.equal(0, len(expected_comment))


def test_create_category(db, category_controller, check, faker):
    data = dict(
        name=faker.word(),
        slug=faker.slug(),
    )
    category = category_controller.create_category(**data)
    expected_category = category_controller.get_category(category.id)
    check.equal(category, expected_category)


def test_create_language(db, language_controller, check, faker):
    data = dict(
        name=faker.word(),
        slug=faker.slug(),
    )
    language = language_controller.create_language(**data)
    expected_language = language_controller.get_language(language.id)
    check.equal(language, expected_language)


def test_create_author(db, author_controller, check, faker):
    data = dict(
        name=faker.word(),
        slug=faker.slug(),
        bio=faker.text(),
    )
    author = author_controller.create_author(**data)
    expected_author = author_controller.get_author(author.id)
    check.equal(author, expected_author)


def test_create_book(db, book_controller, check, faker, author_factory, category_factory, language_factory):
    data = dict(
        category=category_factory(),
        author=author_factory(),
        language=language_factory(),
        name=faker.word(),
        slug=faker.slug(),
        price=faker.random_int(),
        stock=faker.random_int(),
        available=faker.boolean(),
        description=faker.text(),
        image=faker.image_url(),
    )
    book = book_controller.create_book(**data)
    expected_book = book_controller.get_book(book.id)
    check.equal(book, expected_book)


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_create_comment(db, comment_controller, check, faker, book_factory, profile_factory):
    data = dict(
        book=book_factory(),
        profile=profile_factory(),
        body=faker.text(),
    )
    comment = comment_controller.create_comment(**data)
    expected_comment = comment_controller.get_comment(comment.id)
    check.equal(comment, expected_comment)
