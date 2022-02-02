from django.urls import path
from authentication.views import RegisterAPIView, LoginAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
]
