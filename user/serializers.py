from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = User
        fields = ['username', 'password']

    def validate_password(self, value: str) -> str:
  
        return make_password(value)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['password'] = user.password
    
        return token