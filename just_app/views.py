from django.shortcuts import render
from .models import Book, Author, Publisher
from django.db.models import Count, F

def hello(request):
    result = (
        Book
        .objects
        .values('publisher')
        .annotate(books_count=Count(F('title')), name = F('publisher__name'))
    )

    return render(request, 
              'index.html', 
              { 'results': result})