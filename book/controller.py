from django.contrib.auth.models import User
from book.models import Category, Book, Comment, Author


class CategoryController:

    def get_category(self, category_id):
        return Category.objects.get(pk=category_id)

    def create_category(self, **data):
        category = Category(**data)
        category.save()
        return category

    def list_categories_by_filters(self, name=None, slug=None):
        query = Category.objects.all()
        if name:
            query = query.filter(name=name)
        if slug:
            query = query.filter(slug=slug)
        return query.all()


class AuthorController:

    def get_author(self, author_id):
        return Author.objects.get(pk=author_id)

    def create_author(self, **data):
        author = Author(**data)
        author.save()
        return author

    def list_authors_by_filters(self, name=None):
        query = Author.objects.all()
        if name:
            query = query.filter(name=name)
        return query.all()


class BookController:

    def get_book(self, book_id):
        return Book.objects.get(pk=book_id)

    def create_book(self, **data):
        book = Book(**data)
        book.save()
        return book

    def list_books_by_filters(self, name=None, category=None, author=None, language=None):
        query = Book.objects.all()
        if name:
            query = query.filter(name=name)
        if category:
            query = query.filter(categories=category)
        if author:
            query = query.filter(authors=author)
        if language:
            query = query.filter(language=language)
        return query.all()


class CommentController:

    def get_comment(self, comment_id):
        return Comment.objects.get(pk=comment_id)

    def create_comment(self, **data):
        comment = Comment(**data)
        comment.save()
        return comment

    def list_comments_by_filters(self, book=None, user=None, rate=None):
        query = Comment.objects.all()
        if book:
            query = query.filter(books=book)
        if user:
            query = query.filter(users=user)
        if rate:
            query = query.filter(rate=rate)
        return query.all()


class UserController:

    def get_user(self, user_id):
        return User.objects.get(pk=user_id)

    def create_user(self, **data):
        user = User(**data)
        user.save()
        return user

    def list_users_by_filters(self, first_name=None):
        query = User.objects.all()
        if first_name:
            query = query.filter(first_name=first_name)
        return query.all()


category_controller = CategoryController()
author_controller = AuthorController()
book_controller = BookController()
comment_controller = CommentController()
user_controller = UserController()
