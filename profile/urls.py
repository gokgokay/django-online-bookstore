from django.urls import path
from profile import views

urlpatterns = [
    path('user-profiles/', views.ProfileList.as_view(), name='user-profiles'),
]