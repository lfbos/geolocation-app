# Generated by Django 3.2.9 on 2021-11-15 00:09

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='currency name')),
                ('code', models.CharField(max_length=64, verbose_name='currency code')),
            ],
            options={
                'verbose_name': 'currency',
                'verbose_name_plural': 'currencies',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='language name')),
                ('code', models.CharField(max_length=64, verbose_name='language code')),
            ],
            options={
                'verbose_name': 'language',
                'verbose_name_plural': 'languages',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=128, verbose_name='provider name')),
                ('email', models.EmailField(error_messages={'unique': 'A provider with that email already exists.'}, max_length=254, unique=True, verbose_name='email address')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='phone number')),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='providers', to='providers.currency')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='providers', to='providers.language')),
            ],
            options={
                'verbose_name': 'provider',
                'verbose_name_plural': 'providers',
            },
        ),
    ]
