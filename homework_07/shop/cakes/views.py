from django.shortcuts import render
from cakes.models import Cake
# Create your views here.
# views = controllers

def main_page(request):
    cakes = Cake.objects.all()
    context = {
        'cakes': cakes
    }
    return render(request, 'cakes/index.html', context=context)