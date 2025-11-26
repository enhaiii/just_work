from django.shortcuts import HttpResponse, render, get_object_or_404
from .models import Item, Manufacturer
from django.db.models import F, Sum

def add_item(request):

    manufacturer = get_object_or_404(
        Manufacturer,
        name = 'Рога и копыта'
    )
    name = request.POST.get('item_name', '')
    price = request.POST.get('price', '')
    quantity = request.POST.get('quantity', '')
    
    if name and price and quantity:
        item = Item(
            name = name,
            price = price,
            quantity = quantity,
            manufacturer=manufacturer,
        )
        item.save()

    context = {
    }

    return render(request, 'index.html', context)