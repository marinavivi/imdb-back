from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=128, min_length=8, required=True)
    description = serializers.CharField(max_length=500, min_length=8, required=True)

    class Meta:
        
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        movie = Movie.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            coverImage=validated_data['coverImage'],
        )
        movie.save()

        return movie
        