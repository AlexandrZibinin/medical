from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    name = models.CharField(max_length=100, verbose_name="Имя Фамилия")

    token = models.CharField(
        max_length=100, verbose_name="Токен", **NULLABLE
    )

    avatar = models.ImageField(
        upload_to="users/avatars", **NULLABLE, verbose_name="Аватар"
    )
    token = models.CharField(max_length=100, verbose_name="token", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
