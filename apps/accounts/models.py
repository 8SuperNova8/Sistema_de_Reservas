from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    #campo que se usará para autenticación
    USERNAME_FIELD = 'email'
    #campos que se piden al crear el super usuario
    REQUIRED_FIELDS = []

    objects= CustomUserManager()
