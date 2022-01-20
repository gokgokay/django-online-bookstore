from django.urls import path
from profile import views
from profile.views import ProfileRetrieveAPIView, ProfileCreateList

urlpatterns = [
    path('profile/<username>/', ProfileCreateList.as_view(), name='user-profiles'),
    path('profile/<username>/follow/', ProfileRetrieveAPIView.as_view(), name='user-profile-follows'),
]