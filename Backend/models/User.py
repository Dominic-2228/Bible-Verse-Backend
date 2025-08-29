# Backend/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Keep first_name and last_name from AbstractUser
    profilePhoto = models.CharField(max_length=500, blank=True, null=True)  # store URL or file path