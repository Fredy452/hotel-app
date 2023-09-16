"""Users models."""

# Django
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile models class."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Agregar las propiedades (atributos)
    