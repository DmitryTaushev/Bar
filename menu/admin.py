from django.contrib import admin

from menu.models import Category,DrinkAndDish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    ordering = ('pk',)


@admin.register(DrinkAndDish)
class DrinkAndDishAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category')
    list_filter = ('category',)
    ordering = ('name',)

