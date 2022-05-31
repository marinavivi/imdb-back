from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginViewSet(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
