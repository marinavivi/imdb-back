from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(('email'), unique=True)
    username = models.CharField('username', unique=False, max_length=255)
    REQUIRED_FIELDS = []

