from django.urls import path, include
from .views import (
    CategoryListAPIView,
    AuthorListAPIView,
    BookListAPIView,
    CommentsListCreateAPIView,
    CommentUpdateDestroyAPIView)


urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='categories'),
    path('author/', AuthorListAPIView.as_view(), name='authors'),
    path('book/', BookListAPIView.as_view(), name='books'),
    path('book/<book_slug>/comment/', CommentsListCreateAPIView.as_view(), name='comment'),
    path('book/<book_slug>/comment/<comment_pk>/', CommentUpdateDestroyAPIView.as_view(), name='comment')
]
