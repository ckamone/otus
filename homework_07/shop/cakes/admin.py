from django.contrib import admin
from cakes.models import (
    Cake,
    CakeType,
    Ingredient,
    Card,
)
# Register your models here.

admin.site.register(CakeType)
admin.site.register(Cake)
admin.site.register(Ingredient)
admin.site.register(Card)