from django.db import models
from django.conf import settings

from users.models import User,NULLABLE

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.CharField(max_length=1000, verbose_name='Описание')
    photo = models.ImageField(upload_to='drinks/', **NULLABLE, verbose_name='Фото')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class DrinkAndDish(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    photo = models.ImageField(upload_to='drinks/', **NULLABLE, verbose_name='Фото')
    price = models.IntegerField(default=0,verbose_name='Цена')
    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'drinkanddish'
        verbose_name_plural = 'drinksanddishes'

class CartItem(models.Model):
    product = models.ForeignKey(DrinkAndDish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,**NULLABLE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'


