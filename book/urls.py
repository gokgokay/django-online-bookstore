from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CategoryListAPIView, AuthorListAPIView, BookListAPIView, CommentListAPIView, CommentsDestroyAPIView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='categories'),
    path('author/', AuthorListAPIView.as_view(), name='authors'),
    path('book/', BookListAPIView.as_view(), name='books'),
    path('comment/', CommentListAPIView.as_view(), name='comments'),
]
