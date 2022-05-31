from django.db import models

class Genre(models.Model):

    name = models.CharField(max_length=128, blank=False, null = False, unique=True)
