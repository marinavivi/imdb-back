from django.shortcuts import render
from .serializers import GenreSerializer
from rest_framework import viewsets
from .models import Genre
from rest_framework.response import Response
from rest_framework import status

class GenreViewSet(viewsets.ModelViewSet):

    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    def create(self, request, *args, **kwargs):
       
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)