from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from user.models import User
from rest_framework.response import Response
from rest_framework import status

class LoginViewSet(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        permission_classes = [AllowAny]
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        
        return Response(status=status.HTTP_201_CREATED)