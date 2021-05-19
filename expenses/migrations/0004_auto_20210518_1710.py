# Generated by Django 3.2.3 on 2021-05-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_auto_20210518_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(blank=True, choices=[('ONLINE_SERVICES', 'ONLINE_SERVICES'), ('TRAVEL', 'TRAVEL'), ('FOOD', 'FOOD'), ('RENT', 'RENT'), ('OTHERS', 'OTHERS')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]