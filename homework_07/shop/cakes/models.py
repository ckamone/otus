from django.db import models

# Create your models here.

# cake (name, price, ingridients)
# cake types (type name: chocolate, carrot, yoghurt, ice cream, mousse, cheese)
# cake ingridients (name)
# cake card (name, photo, about)


class CakeType(models.Model):
    type = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.type


class Ingredient(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Cake(models.Model):
    name = models.CharField(max_length=64)
    type = models.ForeignKey(CakeType, on_delete=models.CASCADE) # one to many
    price = models.IntegerField(verbose_name='price', default=0)
    description = models.TextField(verbose_name='description', blank=True)
    ingredients = models.ManyToManyField(Ingredient)  # many to many
    weight = models.IntegerField(verbose_name='weight', default=0)

    def __str__(self):
        return f'{self.name} ({self.price}$)'


class Card(models.Model):
    text = models.TextField(blank=True)
    cake = models.OneToOneField(Cake, on_delete=models.CASCADE) # one to one

    def __str__(self):
        return f'{self.cake}: {self.text}'


