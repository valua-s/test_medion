from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import REQUIRED_FIELD_MAX_LENGTH


class Position(models.Model):
    name = models.CharField(
        'Название должности', max_length=REQUIRED_FIELD_MAX_LENGTH,
    )

    class Meta:
        verbose_name = "должность"
        verbose_name_plural = "должности"
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class User(AbstractUser):
    username = models.CharField(
        'Ник пользователя', max_length=REQUIRED_FIELD_MAX_LENGTH,
        unique=True)
    password = models.CharField(
        'Пароль', max_length=REQUIRED_FIELD_MAX_LENGTH,
    )
    role = models.CharField(
        'Роль', max_length=10, default='user'
    )

    class Meta:
        verbose_name = "пользователя"
        verbose_name_plural = "пользователи"
        ordering = ['date_joined']

    def __str__(self):
        return f'{self.username}'


class Employee(models.Model):
    position = models.ForeignKey(Position, verbose_name='Должность',
                                 on_delete=models.SET_NULL,
                                 null=True,)
    is_fired = models.BooleanField('Уволен ли сотрудник', blank=True,
                                   null=True, default=False)
    fire_date = models.DateField('Дата увольнения', blank=True,
                                 null=True)
    last_name = models.CharField(
        'Фамилия сотрудника', max_length=REQUIRED_FIELD_MAX_LENGTH,
    )
    first_name = models.CharField(
        'Имя сотрудника', max_length=REQUIRED_FIELD_MAX_LENGTH,
    )
    patronymic = models.CharField(
        'Отчество сотрудника', max_length=REQUIRED_FIELD_MAX_LENGTH,
    )

    class Meta:
        verbose_name = "сотрудик"
        verbose_name_plural = "сотрудники"
        unique_together = ('last_name', 'first_name', 'patronymic',
                           'fire_date', 'position')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
