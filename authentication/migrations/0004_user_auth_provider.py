# Generated by Django 3.2.3 on 2021-05-20 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_rename_is_stuff_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_provider',
            field=models.CharField(default='email', max_length=255),
        ),
    ]
