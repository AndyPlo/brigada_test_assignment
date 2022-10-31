from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class City(models.Model):
    city_name = models.CharField(
        'Название города',
        max_length=30,
        unique=True
    )

    class Meta:
        ordering = ['city_name']
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.city_name


class Brigada(models.Model):
    brigada_name = models.CharField(
        'Бригада',
        max_length=30,
        unique=True
    )
    people_amount = models.IntegerField(
        blank=True,
        null=True
    )
    name_responsible = models.CharField(
        'Ф.И.О. ответственного',
        max_length=30,
        blank=True,
        null=True
    )
    position_responsible = models.CharField(
        'Должность ответственного',
        max_length=30,
        blank=True,
        null=True
    )
    rank_responsible = models.IntegerField(
        'Разряд ответственного',
        validators=[MinValueValidator(1), MaxValueValidator(8)],
        blank=True,
        null=True
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='brigadas',
        verbose_name='Город'
    )

    class Meta:
        ordering = ['brigada_name']
        verbose_name = 'Бригада'
        verbose_name_plural = 'Бригады'

    def __str__(self):
        return f'{self.brigada_name} ({self.city})'


class Object(models.Model):
    object_name = models.CharField(
        'Объект',
        max_length=30,
        unique=True
    )
    people_amount = models.IntegerField(
        blank=True,
        null=True
    )
    name_responsible = models.CharField(
        'Ф.И.О. ответственного',
        max_length=30,
        blank=True,
        null=True
    )
    position_responsible = models.CharField(
        'Должность ответственного',
        max_length=30,
        blank=True,
        null=True
    )
    rank_responsible = models.IntegerField(
        'Разряд ответственного',
        validators=[MinValueValidator(1), MaxValueValidator(8)],
        blank=True,
        null=True
    )
    brigada = models.ForeignKey(
        Brigada,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='object_list',
        verbose_name='Бригада'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='object_list',
        verbose_name='Город'
    )

    class Meta:
        ordering = ['object_name']
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return f'{self.object_name} ({self.city})'
