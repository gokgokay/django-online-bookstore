from rest_framework import generics, status, serializers
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.response import Response
from book.permissions import IsOwnerOrReadOnly
from book.serializers import FavoriteBookSerializer
from .models import Book, Comment
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from .renderers import CategoryJSONRenderer, LanguageJSONRenderer, AuthorJSONRenderer, BookJSONRenderer, \
    CommentJSONRenderer
from .serializers import CategorySerializer, AuthorSerializer, BookSerializer, CommentSerializer, LanguageSerializer
from book.controllers import (category_controller, language_controller, author_controller, book_controller,
                              comment_controller)


class CategoryListAPIView(generics.ListAPIView):
    queryset = category_controller.list_categories_by_filters()
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    # renderer_classes = [CategoryJSONRenderer]

    def list(self, request, *args, **kwargs):
        serializer_data = self.get_queryset()
        serializer = self.serializer_class(serializer_data, many=True)

        return Response({
            'status': status.HTTP_200_OK,
            'categories': serializer.data})


class LanguageListAPIView(generics.ListAPIView):
    queryset = language_controller.list_languages_by_filters()
    permission_classes = (AllowAny,)
    serializer_class = LanguageSerializer
    # renderer_classes = [LanguageJSONRenderer]

    def list(self, request, *args, **kwargs):
        serializer_data = self.get_queryset()
        serializer = self.serializer_class(serializer_data, many=True)

        return Response({
            'status': status.HTTP_200_OK,
            'languages': serializer.data})


class AuthorListAPIView(generics.ListAPIView):
    queryset = author_controller.list_authors_by_filters()
    permission_classes = (AllowAny,)
    serializer_class = AuthorSerializer
    # renderer_classes = [AuthorJSONRenderer]

    def list(self, request, *args, **kwargs):
        serializer_data = self.get_queryset()
        serializer = self.serializer_class(serializer_data, many=True)

        return Response({
            'status': status.HTTP_200_OK,
            'authors': serializer.data})


class BookListAPIView(generics.ListAPIView):
    queryset = book_controller.list_books_by_filters()
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer
    # renderer_classes = [BookJSONRenderer]

    def list(self, request, *args, **kwargs):
        serializer_data = self.get_queryset()
        serializer = self.serializer_class(serializer_data, many=True)

        return Response({
            'status': status.HTTP_200_OK,
            'books': serializer.data})


class CommentsListCreateAPIView(generics.ListCreateAPIView):
    lookup_url_kwarg = 'book_slug'
    queryset = Comment.objects.select_related('book', 'profile')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CommentSerializer
    # renderer_classes = [CommentJSONRenderer]

    def list(self, request, *args, **kwargs):
        serializer_data = self.get_queryset()
        serializer = self.serializer_class(serializer_data, many=True)

        return Response({
            'status': status.HTTP_200_OK,
            'comments': serializer.data})

    def create(self, request, book_slug=None, *args, **kwargs):
        data = request.data
        context = {'profile': request.user.profile}

        try:
            context['book'] = Book.objects.get(slug=book_slug)
        except ObjectDoesNotExist:
            raise NotFound('No book found with this slug')

        serializer = self.serializer_class(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'status': status.HTTP_200_OK,
            'comments': serializer.data})


class CommentUpdateDestroyAPIView(generics.DestroyAPIView,
                                  generics.UpdateAPIView):
    lookup_url_kwarg = 'comment_pk'
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = CommentSerializer
    queryset = comment_controller.list_comments_by_filters()


class BookFavoriteAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FavoriteBookSerializer

    def post(self, request, book_slug=None):
        profile = request.user.profile
        serializer_context = {'request': request}

        try:
            book = Book.objects.get(slug=book_slug)
        except ObjectDoesNotExist:
            raise NotFound('No article with this slug')

        if profile.has_favorited(book):
            raise serializers.ValidationError('You already favorite this book')

        profile.favorite(book)
        serializer = self.serializer_class(book, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, book_slug=None):
        profile = request.user.profile
        serializer_context = {'request': request}

        try:
            book = Book.objects.get(slug=book_slug)
        except ObjectDoesNotExist:
            raise NotFound('No article with this slug')

        if not profile.has_favorited(book):
            raise NotFound('You already unfavorite this book')

        profile.unfavorite(book)
        serializer = self.serializer_class(book, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
