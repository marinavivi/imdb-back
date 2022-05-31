from rest_framework import routers
from django.urls import path, include
from movie import views

router = routers.DefaultRouter()

router.register('movies', viewset=views.MovieViewSet)

urlpatterns = [
    path('',include(router.urls)),
]