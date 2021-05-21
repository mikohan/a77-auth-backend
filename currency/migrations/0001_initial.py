# Generated by Django 3.2.3 on 2021-05-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsdRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=5, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Dollar Rate',
            },
        ),
    ]
