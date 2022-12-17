from django.core.management.base import BaseCommand
from cakes.models import CakeType, Cake, Card, Ingredient

class Command(BaseCommand):
    help = 'Fill DB'

    def handle(self, *args, **options):
        # create, update, delete, viborka vseh, viborka 1
        # 1 DELETE
        print('start')
        print('delete old data')
        CakeType.objects.all().delete()
        Cake.objects.all().delete()
        Card.objects.all().delete()
        Ingredient.objects.all().delete()
        print('end')

        # 2 CREATE
        print('create new Type')
        type_choco = CakeType.objects.create(type='Carrot')
        print(type_choco.type)
        type_cheese = CakeType.objects.create(type='Cheese')
        print(type_cheese.type)
        print('end')

        # 3 Update
        type_choco.type = 'Chocolate'
        type_choco.save()
        print(type_choco.type)

        sugar = Ingredient.objects.create(name='Sugar')
        sour = Ingredient.objects.create(name='Sour')
        chocolate = Ingredient.objects.create(name='Chocolate')
        peanut = Ingredient.objects.create(name='Peanut')
        egg = Ingredient.objects.create(name='Egg')
        cacao = Ingredient.objects.create(name='Cacao')

        cake_choco = Cake.objects.create(
            name="Snickers",
            type=type_choco,
            price=45,
            weight=2,
        )

        cake_choco.ingredients.add(
            sugar, peanut,
            sour, chocolate,
            egg, cacao,
        )
        cake_choco.save()

        print(cake_choco)
        card_choco = Card.objects.create(
            cake=cake_choco,
            text='Внутри начинка «Сникерс». '
                 'Шоколадный бисквит, соленый арахис, '
                 'безе и сладкий-сладкий крем.',
        )
        print(card_choco)

        cheese_cake = Cake.objects.create(
            name="New-York",
            type=type_cheese,
            price=20,
            weight=1,
        )
        print(cheese_cake)
        card_chese = Card.objects.create(
            cake=cheese_cake,
            text='Нежнейший, тающий во рту, оставляющий удивительное '
                 'послевкусие - это все об этой уникальной новинке. '
                 'Упаковка товара удобная, не громоздкая. Цена - демократичная. '
                 'Чизкейк обязательно станет прекрасным дополнением к '
                 'чаепитию с семьей. Попробуйте, не пожалеете!',
        )
        print(card_chese)

        cheese = Ingredient.objects.create(name='Cheese')
        salt = Ingredient.objects.create(name='Salt')
        milk = Ingredient.objects.create(name='Milk')
        cheese_cake.ingredients.add(
            sugar, sour,
            egg, cheese,
            salt, milk
        )
        cheese_cake.save()

        cakes = Cake.objects.all()
        print(type(cakes))
        for cake in cakes:
            print(f'{cake.name} ({cake.type})')
            for num, ingredient in enumerate(cake.ingredients.all()):
                print(num+1, ingredient.name)
            print()

        # find
        cheese_cake_id = cheese_cake.id
        one_cake = Cake.objects.get(id=cheese_cake_id)
        print(one_cake)

        one_cake = Cake.objects.filter(id=cheese_cake_id).first()
        print(one_cake)

        # filter
        # by name
        cakes_filt = Cake.objects.filter(name='Snickers')
        print(cakes_filt)
