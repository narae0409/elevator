# Generated by Django 3.1.1 on 2020-11-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevator_api', '0004_auto_20201109_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='my_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
