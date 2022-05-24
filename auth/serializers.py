from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from user.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class LoginSerializer(TokenObtainPairSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']

    def get_token(cls, user):
        
        token = super(LoginSerializer, cls).get_token(user)

        token['email'] = user.email
        token['password'] = user.password
    
        return token

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
            required=True,
            )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user