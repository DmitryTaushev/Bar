from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=100,verbose_name='name')
    description = models.CharField(max_length=1000, verbose_name='description')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'name'
        verbose_name_plural = 'names'
