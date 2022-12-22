from django.shortcuts import render
from django.urls import reverse_lazy

from cakes.models import Cake, CakeType, Ingredient
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView,
)
# Create your views here.
# views = controllers

def main_page(request):
    return render(request, 'cakes/index.html')

#def categories_page(request):
#    types = CakeType.objects.all()
#    context = {
#        'types': types
#    }
#    return render(request, 'cakes/categories.html', context=context)

#def products_page(request):
#    cakes = Cake.objects.all()
#    context = {
#        'cakes': cakes
#    }
#    return render(request, 'cakes/products.html', context=context)


class CakeTypeListView(ListView):
    model = CakeType


class CakeTypeCreateView(CreateView):
    model = CakeType
    fields = '__all__'
    success_url = reverse_lazy('categories_page')


class CakeTypeUpdateView(UpdateView):
    model = CakeType
    fields = '__all__'
    success_url = reverse_lazy('categories_page')


class CakeTypeDeleteView(DeleteView):
    model = CakeType
    success_url = reverse_lazy('categories_page')


class IngredientListView(ListView):
    model = Ingredient


class IngredientCreateView(CreateView):
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('ingredients_page')


class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('ingredients_page')


class IngredientDeleteView(DeleteView):
    model = Ingredient
    success_url = reverse_lazy('ingredients_page')


class CakeListView(ListView):
    model = Cake


class CakeDetailView(DetailView):
    model = Cake


class CakeCreateView(CreateView):
    model = Cake
    fields = '__all__'
    success_url = reverse_lazy('cakes_page')

class CakeUpdateView(UpdateView):
    model = Cake
    fields = '__all__'
    success_url = reverse_lazy('cakes_page')


class CakeDeleteView(DeleteView):
    model = Cake
    success_url = reverse_lazy('cakes_page')