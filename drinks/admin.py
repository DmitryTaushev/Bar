from django.contrib import admin

from drinks.models import Type, Drink

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('pk','name')
    ordering = ('pk',)

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('pk','name','alco',)
    list_filter = ('alco',)
    ordering = ('name',)