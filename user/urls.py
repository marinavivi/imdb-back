from rest_framework import routers
from django.urls import path, include
from user import views

from user import views

router = routers.DefaultRouter()

router.register('users', viewset=views.UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
]