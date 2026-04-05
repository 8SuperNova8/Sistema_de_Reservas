from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    is_staff = None
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    #campo que se usará para autenticación
    USERNAME_FIELD = 'email'
    #campos que se piden al crear el super usuario
    REQUIRED_FIELDS = []
