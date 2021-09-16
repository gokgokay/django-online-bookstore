from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryCreateList.as_view(), name='category-create-list'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='category-detail'),
    path('author/', views.AuthorCreateList.as_view(), name='author-create-list'),
    path('author/<int:pk>', views.AuthorDetail.as_view(), name='author-detail'),
    path('book/', views.BookCreateList.as_view(), name='book-create-list'),
    path('book/<uuid:pk>', views.BookDetail.as_view(), name='book-detail'),
    path('book/<uuid:book_pk>/comment', views.CommentCreate.as_view(), name='comment-create'),
    path('comment/<int:pk>', views.CommentDetail.as_view(), name='comment-detail'),

]
