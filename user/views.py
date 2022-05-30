from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [AllowAny]

    def retrieve(self, request, pk=None):
        permission_classes = [AllowAny]
        if request.user and pk == 'me':
            return Response(UserSerializer(request.user).data)
        return super(UserViewSet, self).retrieve(request, pk)
       