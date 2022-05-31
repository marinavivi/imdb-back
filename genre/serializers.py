from rest_framework import serializers
from .models import Genre
from rest_framework.validators import UniqueValidator

class GenreSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=128, required=True, validators=[UniqueValidator(queryset=Genre.objects.all())])

    class Meta:
        model = Genre
        fields = ['id', 'name']

def create(self, validated_data):
        genre = Genre.objects.create(
            name=validated_data['name'],
        )
        genre.save()

        return genre
        