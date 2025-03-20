from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuarios(AbstractUser):
    nome = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email
