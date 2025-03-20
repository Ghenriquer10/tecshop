from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Gerenciador para o modelo de usuário personalizado."""

    def create_user(self, email, password=None, **extra_fields):
        """Cria e retorna um usuário comum com email e senha."""
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Cria e retorna um superusuário."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superusuário precisa ter is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superusuário precisa ter is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class Usuarios(AbstractUser):
    """Modelo de usuário personalizado."""

    username = None  # Removemos o campo username
    nome = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    objects = UserManager()  # Define o UserManager personalizado

    USERNAME_FIELD = "email"  # Define o campo usado para login
    REQUIRED_FIELDS = ["nome"]  # Define os campos obrigatórios além do email

    def __str__(self):
        return self.email
