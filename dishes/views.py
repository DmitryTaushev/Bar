from django.shortcuts import render

from dishes.models import Dish

def dishes_list_view(request):
    context = {
        'objects_list': Dish.objects.all()[:2],
        'title': "Блюда"

    }
    return render(request, 'dishes/dishes.html',context=context)