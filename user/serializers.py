from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = User
        fields = ['email', 'first_name', 'password']

    def validate_password(self, value: str) -> str:
  
        return make_password(value)