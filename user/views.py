from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User

from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [AllowAny]

    def retrieve(self, request, pk=None):
        if request.user and pk == 'me':
            return Response(UserSerializer(request.user).data)
        return super(UserViewSet, self).retrieve(request, pk)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer

# from rest_framework import mixins

# class UserViewSet(mixins.CreateModelMixin,
#                                 mixins.ListModelMixin,
#                                 mixins.RetrieveModelMixin,
#                                 viewsets.GenericViewSet):
    
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
    
#     def get_permissions(self):
#         permission_classes = [AllowAny]
#         if self.action == 'retrieve':
#             permission_classes = [IsAdminUser]
        
#         return [permission() for permission in permission_classes]
