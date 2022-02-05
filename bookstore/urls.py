from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('book.urls')),
    path('api/', include('profile.urls')),
    path('api/', include('authentication.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api/users/login', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/password/reset/', include('rest_auth.urls')),
    url(r'^rest-auth/password/reset/confirm/', include('rest_auth.urls')),
    url(r'^rest-auth/password/change/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/verify-email/', include('rest_auth.urls')),
    url(r'^rest-auth/logout', include('rest_auth.urls')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
