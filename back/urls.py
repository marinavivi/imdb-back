from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from auth.views import LoginViewSet, RegisterViewSet

urlpatterns = [

    path('admin/', admin.site.urls),

    path('login/', LoginViewSet.as_view(), name='login_viewset'),
    path('register/', RegisterViewSet.as_view({'post': 'create'}), name='register_viewset'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('',include('user.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
