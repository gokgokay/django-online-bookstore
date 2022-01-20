from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Category, Author, Book, Comment
from .renderers import CategoryJSONRenderer, AuthorJSONRenderer, BookJSONRenderer, CommentJSONRenderer
from .serializers import CategorySerializer, AuthorSerializer, BookSerializer, CommentSerializer
from book.permissions import IsAdminUserOrReadOnly, IsUserOrReadOnly


class CategoryCreateList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    # renderer_classes = [CategoryJSONRenderer]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    # renderer_classes = [CategoryJSONRenderer]


class AuthorCreateList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    # renderer_classes = [AuthorJSONRenderer]


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]
    # renderer_classes = [AuthorJSONRenderer]


class BookCreateList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    # renderer_classes = [BookJSONRenderer]


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    # renderer_classes = [BookJSONRenderer]


class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # renderer_classes = [CommentJSONRenderer]

    def perform_create(self, serializer):
        book_pk = self.kwargs.get('book_pk')
        book = get_object_or_404(Book, pk=book_pk)
        user = self.request.user
        comments = Comment.objects.filter(books=book, users=user)
        if comments.exists():
            raise ValidationError('You can only make one comment on a book.')
        serializer.save(books=book, users=user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsUserOrReadOnly]
    # renderer_classes = [CommentJSONRenderer]
