# Generated by Django 3.2.3 on 2021-05-21 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='_price',
        ),
    ]
