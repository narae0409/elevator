# Generated by Django 3.1.1 on 2020-10-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevator_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default='2020-01-01 00:00'),
            preserve_default=False,
        ),
    ]