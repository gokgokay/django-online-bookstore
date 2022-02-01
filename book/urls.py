from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CategoryViewSet, AuthorViewSet, BookViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'book', BookViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
