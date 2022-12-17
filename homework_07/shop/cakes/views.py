from django.shortcuts import render

# Create your views here.
# views = controllers

def main_page(request):
    return render(request, 'cakes/index.html')