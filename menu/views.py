from django.shortcuts import render, get_object_or_404, redirect
# from django.template.context_processors import request
# from django.http import Http404
from django.urls import reverse, reverse_lazy
# from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.db.models import Q

from menu.models import Category, DrinkAndDish
from menu.forms import CategoryForm,DrinkAndDishForm
from users.models import UserRoles

def index_view(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'КрепкоеХмельное-Ассортимент'
    }
    return render(request, 'menu/index.html', context=context)

class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Ассортимент'
    }
    template_name = 'menu/category.html'

class DrinkAndDishCategoryListView(LoginRequiredMixin, ListView):
    model = DrinkAndDish
    template_name = 'menu/drinksanddishes.html'
    extra_context = {
        'title': 'Ассортимент'
    }

    def get_queryset(self):
        queryset = super().get_queryset().filter(category_id=self.kwargs.get('pk'))
        return queryset

class DrinkAndDishListView(LoginRequiredMixin, ListView):
    model = DrinkAndDish
    template_name = 'menu/drinksanddishes.html'
    extra_context = {
        'title': 'Ассортимент'
    }

class DrinkAndDishCreateView(LoginRequiredMixin, CreateView):
    model = DrinkAndDish
    form_class = DrinkAndDishForm
    template_name = 'menu/create.html'
    extra_context = {
        'title': 'Добавить напиток или блюдо'
    }
    success_url = reverse_lazy('menu:all')
