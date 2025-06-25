from django.shortcuts import render

from drinks.models import Type, Drink
def index_view(request):
    context = {
        'objects_list':Type.objects.all()[:3],
        'title': 'Крепкое - Хмельное'
    }
    return render(request, 'drinks/index.html',context = context)
