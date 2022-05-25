from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

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