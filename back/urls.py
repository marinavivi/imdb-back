from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from auth.views import LoginViewSet

urlpatterns = [

    path('admin/', admin.site.urls),

    path('login/', LoginViewSet.as_view(), name='login_viewset'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('',include('user.urls')),
    path('',include('movie.urls')),
    path('',include('genre.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
