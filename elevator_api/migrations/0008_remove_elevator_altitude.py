# Generated by Django 3.1.1 on 2020-11-11 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elevator_api', '0007_auto_20201111_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elevator',
            name='altitude',
        ),
    ]