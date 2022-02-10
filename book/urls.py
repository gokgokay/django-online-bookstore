from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CategoryListAPIView,  AuthorListAPIView, BookListAPIView, CommentsListCreateAPIView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='categories'),
    path('author/', AuthorListAPIView.as_view(), name='authors'),
    path('book/', BookListAPIView.as_view(), name='books'),
    path('book/<book_slug>/comment/', CommentsListCreateAPIView.as_view(), name='comment'),
]
