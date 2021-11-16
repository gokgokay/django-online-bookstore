import pytest_check as check


def test_comment_str(comment):
    check.equal(comment.__str__(), f"{str(comment.rate)}")
