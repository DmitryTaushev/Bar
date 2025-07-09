from django.urls import path
from menu.apps import MenuConfig
from django.views.decorators.cache import cache_page, never_cache

from menu.models import DrinkAndDish
from menu.views import IndexListView,CategoryListView,DrinkAndDishCategoryListView,DrinkAndDishListView,DrinkAndDishCreateView

app_name = MenuConfig.name

urlpatterns = [
    # category
    path('',IndexListView.as_view(), name='index'),
    path('category/', CategoryListView.as_view(), name='categories'),
    # menu

    path('category/<int:pk>/', DrinkAndDishCategoryListView.as_view(), name='categories_drinksanddishes'),
    path('drinkanddishes/',DrinkAndDishListView.as_view(),name='all'),
    path('create/',DrinkAndDishCreateView.as_view(),name='create')


    # path('dogs/', DogListView.as_view(), name='dogs_list'),
    # path('dogs/deactivated', DogDeactivatedListView.as_view(), name='dogs_deactivated_list'),
    # path('dogs/search', DogSearchListView.as_view(), name='dog_search'),
    # path('dogs/create', DogCreateView.as_view(), name='dog_create'),
    # path('dogs/detail/<int:pk>/', DogDetailView.as_view(), name='dog_detail'),
    # path('dogs/update/<int:pk>/', never_cache(DogUpdateView.as_view()), name='dog_update'),
    # path('dogs/toggle/<int:pk>/', dog_toggle_activity, name='dog_toggle_activity'),
    # path('dogs/delete/<int:pk>/', DogDeleteView.as_view(), name='dog_delete')
]