from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    https://docs.djangoproject.com/en/1.11/ref/contrib/auth/#user-model
    """

    direccion1 = models.CharField(max_length=50, null=True, blank=True)
    direccion2 = models.CharField(max_length=50, null=True, blank=True)
    ciudad = models.CharField(max_length=50, null=True, blank=True)
    provincia = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=32, null=True, blank=True)
