# Generated by Django 3.2 on 2022-12-17 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0003_auto_20221217_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cake',
            old_name='ingredient',
            new_name='ingredients',
        ),
    ]