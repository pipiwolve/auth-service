from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)

# settings.py define specific model
AUTH_USER_MODEL = 'accounts.CustomUser'