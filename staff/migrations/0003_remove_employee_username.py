# Generated by Django 4.0.4 on 2022-05-27 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_employee_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='username',
        ),
    ]
