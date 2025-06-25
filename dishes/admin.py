from django.contrib import admin
from dishes.models import Dish

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('pk','name')
    list_filter = ('name',)