from django.urls import path
from dishes.apps import DishesConfig
from dishes.views import dishes_list_view

app_name = DishesConfig.name

urlpatterns = [
    path('',dishes_list_view,name='dishes')
]
