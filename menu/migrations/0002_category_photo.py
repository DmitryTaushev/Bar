# Generated by Django 5.0.14 on 2025-06-27 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='drinks/', verbose_name='Фото'),
        ),
    ]
