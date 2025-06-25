from django.shortcuts import render

from drinks.models import Type, Drink
def index_view(request):
    context = {
        'objects_list':Type.objects.all()[:2],
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
        'objects_list': Drink.objects.filter(type_id = pk),
        'title':f'Собаки породы - {type_object.name}',
        'type_pk': type_object.pk
    }
    return render(request, 'drinks/drinks.html',context=context)
