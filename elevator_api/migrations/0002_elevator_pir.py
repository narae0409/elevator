# Generated by Django 3.1.1 on 2020-11-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevator_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='elevator',
            name='pir',
            field=models.BooleanField(default=False),
        ),
    ]