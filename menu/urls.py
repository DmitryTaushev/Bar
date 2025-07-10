from django.urls import path
from menu.apps import MenuConfig
from django.views.decorators.cache import cache_page, never_cache

from menu.models import DrinkAndDish
from menu.views import IndexListView,CategoryListView,DrinkAndDishCategoryListView,DrinkAndDishListView,DrinkAndDishCreateView,SearchAllListView,view_cart,add_to_cart,remove_from_cart

app_name = MenuConfig.name

urlpatterns = [
    # category
    path('',IndexListView.as_view(), name='index'),
    path('category/', CategoryListView.as_view(), name='categories'),
    # menu

    path('category/<int:pk>/', DrinkAndDishCategoryListView.as_view(), name='categories_drinksanddishes'),
    path('drinkanddishes/',DrinkAndDishListView.as_view(),name='all'),
    path('create/',DrinkAndDishCreateView.as_view(),name='create'),
    path('menu/search_all/',SearchAllListView.as_view(),name='search_result'),

    path('cart/', view_cart, name='view_cart'),
    path('add/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>/', remove_from_cart, name='remove_from_cart')

]