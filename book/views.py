from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from book.permissions import IsOwnerOrReadOnly
from .models import Category, Author, Book, Comment
from .serializers import CategorySerializer, AuthorSerializer, BookSerializer, CommentSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        serializer_data = self.get_queryset()
        serializer = self.serializer_class(serializer_data, many=True)

        return Response({
            'status': status.HTTP_200_OK,
            'categories': serializer.data})


class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AuthorSerializer

    def list(self, request, *args, **kwargs):
        serializer_data = self.get_queryset()
        serializer = self.serializer_class(serializer_data, many=True)

        return Response({
            'status': status.HTTP_200_OK,
            'authors': serializer.data})


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        serializer_data = self.get_queryset()
        serializer = self.serializer_class(serializer_data, many=True)

        return Response({
            'status': status.HTTP_200_OK,
            'books': serializer.data})


class CommentsListCreateAPIView(generics.ListCreateAPIView):
    lookup_url = 'book_slug'
    queryset = Comment.objects.select_related('book', 'user')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CommentSerializer

    def create(self, request, book_slug=None):
        data = request.data
        context = {'user': request.user}

        try:
            context['book'] = Book.objects.get(slug=book_slug)
        except Book.DoesNotExist:
            raise NotFound('No book found with this slug')

        serializer = self.serializer_class(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'comment': serializer.data,
            'status': status.HTTP_201_CREATED})


class CommentUpdateDestroyAPIView(generics.DestroyAPIView,
                                  generics.UpdateAPIView):
    lookup_url_kwarg = 'comment_pk'
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
