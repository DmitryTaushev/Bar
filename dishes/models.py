from django.db import models

from users.models import NULLABLE

class Dish(models.Model):
    name = models.CharField(max_length=250,verbose_name='dog name')
    photo = models.ImageField(upload_to = 'dishes/',**NULLABLE,verbose_name = 'image')
    description = models.CharField(max_length=1000, verbose_name='description')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'dish'
        verbose_name_plural = 'dishes'
