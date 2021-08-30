from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>', views.CategoryDetail.as_view()),
    path('author/', views.AuthorList.as_view()),
    path('author/<int:pk>', views.AuthorDetail.as_view()),
]
