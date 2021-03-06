from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('book.urls')),
    path('api/', include('profile.urls')),
    path('api/', include('rest_auth.urls')),
    path('api/register/', include('rest_auth.registration.urls')),
    path('api/logout/', include('rest_auth.urls')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
