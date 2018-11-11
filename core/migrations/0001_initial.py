# Generated by Django 2.1.3 on 2018-11-11 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=255)),
                ('ano', models.IntegerField(max_length=255)),
                ('preco', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='carro',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Marca'),
        ),
    ]
