from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,DetailView, UpdateView, DeleteView
from drinks.models import Type, Drink
from drinks.forms import DrinkForm
from dishes.models import Dish
def index_view(request):
    context = {
        'objects_list':Type.objects.all(),
        'title': 'КрепкоеХмельное'
    }
    return render(request, 'drinks/index.html',context = context)

def type_list_view(request):
    context = {
        'objects_list':Type.objects.all(),
        'title': 'Напитки'
    }
    return render(request,'drinks/types.html',context = context)

def type_drink_list_view(request,pk:int):
    type_object = Type.objects.get(pk=pk)
    context = {
        'objects_list': Drink.objects.filter(alco_id = pk),
        'title':f'{type_object.name}',
        'type_pk': type_object.pk
    }
    return render(request, 'drinks/drinks.html',context=context)

class DrinkListView(ListView):
    model = Drink
    extra_context = {
        'title':'Все напитки'
    }

    template_name = 'drinks/drinks.html'