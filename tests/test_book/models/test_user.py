import pytest_check as check


def test_user_str(db, user):
    check.is_(user.__str__(), f"{user.username}")
