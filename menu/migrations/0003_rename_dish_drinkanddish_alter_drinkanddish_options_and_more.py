# Generated by Django 5.0.14 on 2025-06-27 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_category_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dish',
            new_name='DrinkAndDish',
        ),
        migrations.AlterModelOptions(
            name='drinkanddish',
            options={'verbose_name': 'drinkanddish', 'verbose_name_plural': 'drinksanddishes'},
        ),
        migrations.DeleteModel(
            name='Drink',
        ),
    ]
