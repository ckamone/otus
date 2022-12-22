"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from cakes import views

urlpatterns = [
    path('ingredients/', views.IngredientListView.as_view(), name='ingredients_page'),
    path('ingredients/create/', views.IngredientCreateView.as_view(), name='ingredients_create'),
    path('ingredients/update/<int:pk>', views.IngredientUpdateView.as_view(), name='ingredients_update'),
    path('ingredients/delete/<int:pk>', views.IngredientDeleteView.as_view(), name='ingredients_delete'),

    path('categories/', views.CakeTypeListView.as_view(), name='categories_page'),
    path('categories/create/', views.CakeTypeCreateView.as_view(), name='categories_create'),
    path('categories/update/<int:pk>', views.CakeTypeUpdateView.as_view(), name='categories_update'),
    path('categories/delete/<int:pk>', views.CakeTypeDeleteView.as_view(), name='categories_delete'),

    path('cakes/<int:pk>', views.CakeDetailView.as_view(), name='cake_detail'),
    path('cakes/', views.CakeListView.as_view(), name='cakes_page'),
    path('cakes/create/', views.CakeCreateView.as_view(), name='cakes_create'),
    path('cakes/update/<int:pk>', views.CakeUpdateView.as_view(), name='cakes_update'),
    path('cakes/delete/<int:pk>', views.CakeDeleteView.as_view(), name='cakes_delete'),
]
