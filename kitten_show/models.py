from django.db import models
from users.models import CustomUser
from django.conf import settings


class Kitten(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя')
    color = models.CharField(max_length=100, verbose_name='Цвет')
    age = models.SmallIntegerField(verbose_name='Возраст в месяцах',
                                   help_text='Внесите значение возраста в месяцах')
    breed = models.CharField(max_length=255, verbose_name='Порода')
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец',
                              null=True, blank=True, related_name='User_as_course_owner')

    class Meta:
        verbose_name = 'Котенок'
        verbose_name_plural = 'Котята'

    def __str__(self):
        return self.name
