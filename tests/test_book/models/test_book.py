import pytest_check as check


def test_book_str(db, book):
    check.is_(book.__str__(), f"{book.name}")
