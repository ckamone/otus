# Generated by Django 3.2 on 2022-12-17 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0002_rename_ingridient_ingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='cake',
        ),
        migrations.AddField(
            model_name='cake',
            name='ingredient',
            field=models.ManyToManyField(to='cakes.Ingredient'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakes.caketype'),
        ),
        migrations.AlterField(
            model_name='card',
            name='cake',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cakes.cake'),
        ),
    ]