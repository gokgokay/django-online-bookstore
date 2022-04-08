import factory
from django.db.models import signals

from book.models import Category, Language, Author, Book


def test_category_str(db, category_factory, check):
    category = category_factory.create()
    check.is_(category.__str__(), f"{category.name}")


def test_category_save(db, check):
    category = Category(name='Political Thriller')
    category.save()
    check.equal('political-thriller', category.slug)


def test_language_str(db, language_factory, check):
    language = language_factory.create()
    check.is_(language.__str__(), f"{language.name}")


def test_language_save(db, check):
    language = Language(name='English')
    language.save()
    check.equal('english', language.slug)


def test_author_str(db, author_factory, check):
    author = author_factory.create()
    check.is_(author.__str__(), f"{author.name}")


def test_author_save(db, check):
    author = Author(name='Dan Brown')
    author.save()
    check.equal('dan-brown', author.slug)


def test_book_str(db, book_factory, check):
    book = book_factory.create()
    check.is_(book.__str__(), f"{book.name}")


def test_book_save(db, category_factory, author_factory, language_factory, check):
    category = category_factory()
    author = author_factory()
    language = language_factory()
    book = Book(
        category=category,
        author=author,
        language=language,
        price=123.5,
        description='Harvard symbolism professor Robert Langdon wakes up in a hospital in Florence',
        name='In Search of Lost Time'
    )
    book.save()
    check.equal('in-search-of-lost-time', book.slug)


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_comment_str(db, comment_factory, check):
    comment = comment_factory.create()
    check.equal(comment.__str__(), f"{comment.body}")
