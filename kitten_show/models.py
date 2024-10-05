from django.db import models
from users.models import CustomUser
from django.conf import settings
from django.core.validators import MaxValueValidator


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


class Grade(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользовател, поставивший оценку')
    kitten = models.ForeignKey(Kitten, on_delete=models.CASCADE, verbose_name='Котенок, которого оценили')
    value = models.SmallIntegerField(validators=[MaxValueValidator(5)], verbose_name='Значение оценки')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __repr__(self):
        return f'{self.user}; {self.kitten}; {self.value}'
