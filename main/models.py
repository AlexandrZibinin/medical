from django.db import models

from config.settings import NULLABLE
from users.models import User


class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя Фамилия")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    avatar = models.ImageField(
        upload_to="static/doctors", **NULLABLE, verbose_name="Фото"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    price = models.IntegerField(**NULLABLE, verbose_name="цена")
    image = models.ImageField(
        upload_to="static/service", **NULLABLE, verbose_name="Фото"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Appointment(models.Model):
    date_at = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Дата и время посещения")
    service = models.ForeignKey(Service, verbose_name="Услуга", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, verbose_name="Врач", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, verbose_name="Пациент", on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f"{self.owner} в {self.date_at}"

    class Meta:
        verbose_name = "Прием"
        verbose_name_plural = "Приемы"
