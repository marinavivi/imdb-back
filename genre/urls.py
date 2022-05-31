from rest_framework import routers
from django.urls import path, include
from genre import views

router = routers.DefaultRouter()

router.register('genres', viewset=views.GenreViewSet)

urlpatterns = [
    path('',include(router.urls)),
]