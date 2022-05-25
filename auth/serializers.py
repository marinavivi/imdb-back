from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from user.models import User

class LoginSerializer(TokenObtainPairSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']

    def get_token(cls, user):
        
        token = super(LoginSerializer, cls).get_token(user)

        token['email'] = user.email
        token['password'] = user.password
    
        return token
