from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from rest_framework.permissions import AllowAny

class UserSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(max_length=128, min_length=8, required=True)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ['email', 'first_name', 'password']

    def create(self, validated_data):
        permission_classes = [AllowAny]
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user