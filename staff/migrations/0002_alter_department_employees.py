# Generated by Django 4.0.4 on 2022-05-30 04:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='employees',
            field=models.ManyToManyField(related_name='employees', to=settings.AUTH_USER_MODEL),
        ),
    ]
