# Generated by Django 3.1.1 on 2020-11-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevator_api', '0003_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_id', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('permission_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='elevator',
            name='permission_number',
            field=models.IntegerField(default=0),
        ),
    ]