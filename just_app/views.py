from django.shortcuts import HttpResponse, render, get_object_or_404
from .models import Product, Size

def for_product(request):
    all_products = Product.objects.all()

    context = {
        'all_products': all_products,
    }

    return render(request, 'product.html', context)

def for_size(request, product_id: int):

    product = get_object_or_404(Product, article=product_id)
    sizes = Size.objects.filter(art_product=product_id)
    context = {
        'product': product,
        'sizes': sizes,
    }

    return render(request, 'size.html', context)