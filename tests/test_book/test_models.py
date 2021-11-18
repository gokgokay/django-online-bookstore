def test_category_str(db, category_factory, check):
    category = category_factory.create()
    check.is_(category.__str__(), f"{category.name}")


def test_author_str(db, author_factory, check):
    author = author_factory.create()
    check.is_(author.__str__(), f"{author.name}")


def test_book_str(db, book_factory, check):
    book = book_factory.create()
    check.is_(book.__str__(), f"{book.name}")


def test_comment_str(db, comment_factory, check):
    comment = comment_factory.create()
    check.equal(comment.__str__(), f"{str(comment.rate)}")


def test_user_str(db, user_factory, check):
    user = user_factory.create()
    check.is_(user.__str__(), f"{user.username}")
