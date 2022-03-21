import factory
from django.db.models import signals


def test_category_str(db, category_factory, check):
    category = category_factory.create()
    check.is_(category.__str__(), f"{category.name}")


def test_language_str(db, language_factory, check):
    language = language_factory.create()
    check.is_(language.__str__(), f"{language.name}")


def test_author_str(db, author_factory, check):
    author = author_factory.create()
    check.is_(author.__str__(), f"{author.name}")


def test_book_str(db, book_factory, check):
    book = book_factory.create()
    check.is_(book.__str__(), f"{book.name}")


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_comment_str(db, comment_factory, check):
    comment = comment_factory.create()
    check.equal(comment.__str__(), f"{comment.body}")
