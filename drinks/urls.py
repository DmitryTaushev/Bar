from django.urls import path
from drinks.apps import DrinksConfig

from drinks.views import index_view

app_name = DrinksConfig.name

urlpatterns = [
    path('',index_view,name = 'index')
]