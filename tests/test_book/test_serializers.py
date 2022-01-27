from book.serializers import CategorySerializer, AuthorSerializer, BookSerializer, CommentSerializer


def test_serializer_category(db, category_factory, check):
    category = category_factory()
    serializer_category = {
        'id': category.id,
        'name': category.name
    }
    expected_category = CategorySerializer(data=serializer_category)
    check.equal(True, expected_category.is_valid(raise_exception=True))


def test_serializer_author(db, author_factory, check):
    author = author_factory()
    serializer_author = {
        'id': author.id,
        'name': author.slug,
        'bio': author.bio
    }
    expected_author = AuthorSerializer(data=serializer_author)
    check.equal(True, expected_author.is_valid(raise_exception=True))


def test_serializer_comment(db, comment_factory, check):
    comment = comment_factory()
    serializer_comment = {
        'id': comment.id,
        'books': comment.books.id,
        'users': comment.users.id,
        'comment': comment.comment,
        'rate': comment.rate
    }
    expected_comment = CommentSerializer(data=serializer_comment)
    check.equal(True, expected_comment.is_valid(raise_exception=True))


def test_serializer_book(db, book_factory, check):
    book = book_factory()
    serializer_book = {
        'name': book.name,
        'price': book.price,
        'stock': book.stock,
        'available': book.available,
        'description': book.description,
        'language': book.language,
        'categories': book.categories.id,
        'authors': book.authors.id
    }
    expected_book = BookSerializer(data=serializer_book)
    check.equal(True, expected_book.is_valid(raise_exception=True))
