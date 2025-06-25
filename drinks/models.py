from django.db import models
from users.models import NULLABLE

class Type(models.Model):
    name = models.CharField(max_length=100,verbose_name='alco')
    description = models.CharField(max_length=1000, verbose_name='description')
    photo = models.ImageField(upload_to='drinks/', **NULLABLE, verbose_name='image')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'alco'
        verbose_name_plural = 'alcos'

class Drink(models.Model):
    name = models.CharField(max_length=250,verbose_name='name')
    alco = models.ForeignKey(Type, on_delete=models.CASCADE,verbose_name='alco')
    photo = models.ImageField(upload_to = 'drinks/',**NULLABLE,verbose_name = 'image')


    def __str__(self):
        return f'{self.name} ({self.alco})'

    class Meta:
        verbose_name = 'drink'
        verbose_name_plural = 'drinks'