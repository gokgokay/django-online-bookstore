from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile import views
from profile.views import ProfileFollowAPIView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('profiles/<username>/follow/', ProfileFollowAPIView.as_view(), name='user-profiles'),
]
