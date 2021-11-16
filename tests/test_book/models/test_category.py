import pytest_check as check


def test_category_str(db, category):
    check.is_(category.__str__(), f"{category.name}")
