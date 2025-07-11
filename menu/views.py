from itertools import product

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

from menu.models import Category, DrinkAndDish,CartItem
from menu.forms import CategoryForm,DrinkAndDishForm
from users.models import UserRoles

class IndexListView(ListView):
    model = Category
    extra_context = {
        'title': 'Ассортимент'
    }
    template_name = 'menu/index.html'
    paginate_by = 3

class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Ассортимент'
    }
    template_name = 'menu/category.html'
    paginate_by = 3

class DrinkAndDishCategoryListView(ListView):
    model = DrinkAndDish
    template_name = 'menu/drinksanddishes.html'
    extra_context = {
        'title': 'Ассортимент'
    }

    def get_queryset(self):
        queryset = super().get_queryset().filter(category_id=self.kwargs.get('pk'))
        return queryset

class DrinkAndDishListView(ListView):
    model = DrinkAndDish
    template_name = 'menu/drinksanddishes.html'
    extra_context = {
        'title': 'Ассортимент'
    }
    paginate_by = 3

class DrinkAndDishCreateView(LoginRequiredMixin, CreateView):
    model = DrinkAndDish
    form_class = DrinkAndDishForm
    template_name = 'menu/create.html'
    extra_context = {
        'title': 'Добавить напиток или блюдо'
    }
    success_url = reverse_lazy('menu:all')

class SearchAllListView(ListView):
    model = DrinkAndDish
    template_name = 'menu/all_search_result.html'
    extra_context = {
        'title':'Результаты поискового запроса'
    }
    def get_queryset(self):
        query = self.request.GET.get('q')

        drinkanddish_object_list = DrinkAndDish.objects.filter(
            Q(name__icontains=query)
        )
        object_list =list(drinkanddish_object_list)
        return object_list



def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'menu/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, pk:int):
    product = DrinkAndDish.objects.get(pk=pk)
    cart_item, created = CartItem.objects.get_or_create(product=product,
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('menu:view_cart')

def remove_from_cart(request, pk:int):
    cart_item = CartItem.objects.get(pk=pk)
    cart_item.delete()
    return redirect('menu:view_cart')