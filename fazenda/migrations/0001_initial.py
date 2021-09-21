# Generated by Django 3.2.6 on 2021-09-21 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70, unique=True)),
                ('owner', models.CharField(max_length=70)),
                ('cpf', models.BigIntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Farm',
                'verbose_name_plural': 'Farms',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=70)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Seasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70, unique=True)),
                ('latitude', models.CharField(max_length=70, unique=True)),
                ('longitude', models.CharField(max_length=70, unique=True)),
                ('farms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='season', to='fazenda.farms')),
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
            },
        ),
    ]
