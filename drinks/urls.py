from django.urls import path
from drinks.apps import DrinksConfig

from drinks.views import index_view,type_list_view,type_drink_list_view

app_name = DrinksConfig.name

urlpatterns = [
    path('',index_view,name = 'index'),
    path('types/',type_list_view,name='types'),
    path('types/<int:pk>/drinks/',type_drink_list_view,name='type_drink')
]