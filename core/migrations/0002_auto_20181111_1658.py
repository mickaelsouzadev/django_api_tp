# Generated by Django 2.1.3 on 2018-11-11 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='ano',
            field=models.IntegerField(),
        ),
    ]
