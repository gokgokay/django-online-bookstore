import pytest_check as check


def test_author_str(db, author):
    check.is_(author.__str__(), f"{author.name}")
