from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile import views
from profile.views import ProfileFollowAPIView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('profiles/<username>/follow/', ProfileFollowAPIView.as_view(), name='user-profiles'),
    url(r'^profiles/(?P<username>\w+)/follow/?$', ProfileFollowAPIView.as_view()),
]
