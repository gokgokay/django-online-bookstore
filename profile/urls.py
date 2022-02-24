from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile.views import ListProfileView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('profiles/', ListProfileView.as_view()),
]
