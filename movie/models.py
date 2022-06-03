from django.db import models
from genre.models import Genre

class Movie(models.Model):

    title = models.CharField(max_length=50, blank=False, null = False)
    description = models.TextField(max_length=250, blank=True)
    coverImage = models.FileField(blank=False, null=False)
    genre = models.ForeignKey(Genre, related_name='movies', on_delete=models.CASCADE, blank=False, null=True)


