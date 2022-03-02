from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile.views import ListProfileView, RetrieveUpdateProfileView, ProfileFollowAPIView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('profiles/', ListProfileView.as_view()),
    path('profiles/<str:username>/', RetrieveUpdateProfileView.as_view()),
    path('profiles/<str:username>/follow/', ProfileFollowAPIView.as_view())
]
