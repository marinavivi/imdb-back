from django.shortcuts import render
from .serializers import MovieSerializer
from rest_framework import viewsets
from .models import Movie
from rest_framework import filters
import django_filters.rest_framework

class MovieViewSet(viewsets.ModelViewSet):

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    filterset_fields = ['title', 'genre']

def create(self, request, *args, **kwargs):
       
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)