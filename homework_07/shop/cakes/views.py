from django.shortcuts import render
from cakes.models import Cake, CakeType
# Create your views here.
# views = controllers

def main_page(request):
    return render(request, 'cakes/index.html')

def categories_page(request):
    types = CakeType.objects.all()
    context = {
        'types': types
    }
    return render(request, 'cakes/categories.html', context=context)

def products_page(request):
    cakes = Cake.objects.all()
    context = {
        'cakes': cakes
    }
    return render(request, 'cakes/products.html', context=context)