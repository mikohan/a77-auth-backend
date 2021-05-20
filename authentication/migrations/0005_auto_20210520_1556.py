# Generated by Django 3.2.3 on 2021-05-20 15:56

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_user_auth_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=75, size=[100, 100], upload_to='images/users'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
