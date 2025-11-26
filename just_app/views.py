from django.shortcuts import HttpResponse, get_object_or_404
from .models import Item, Manufacturer
from django.db.models import F, Sum

def add_item(request):

    manufacturer =  get_object_or_404(
        Manufacturer,
        name='Бездельники'
    )
    item = Item(
        name = request.GET.get('name', ''),
        price = request.GET.get('price', ''),
        quantity = request.GET.get('quantity', ''),
        manufacturer=manufacturer
    )
    item.save()

    return HttpResponse(status=201)