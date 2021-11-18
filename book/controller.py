from django.contrib.auth.models import User

from book.models import Category, Book, Comment, Author


class CategoryController:

    def get_category(self, category_id):
        return Category.objects.get(pk=category_id)

    def create_category(self, **data):
        category = Category(**data)
        category.save()
        return category


class AuthorController:

    def get_author(self, author_id):
        return Author.objects.get(pk=author_id)

    def create_author(self, **data):
        author = Author(**data)
        author.save()
        return author


class BookController:

    def get_book(self, book_id):
        return Book.objects.get(pk=book_id)

    def create_book(self, **data):
        book = Book(**data)
        book.save()
        return book


class CommentController:

    def get_comment(self, comment_id):
        return Comment.objects.get(pk=comment_id)

    def create_comment(self, **data):
        comment = Comment(**data)
        comment.save()
        return comment


class UserController:

    def get_user(self, user_id):
        return User.objects.get(pk=user_id)

    def create_user(self, **data):
        user = User(**data)
        user.save()
        return user


category_controller = CategoryController()
author_controller = AuthorController()
book_controller = BookController()
comment_controller = CommentController()
user_controller = UserController()
