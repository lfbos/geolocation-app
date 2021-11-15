# Generated by Django 3.2.9 on 2021-11-15 00:09

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=128, verbose_name='service area name')),
                ('price', models.FloatField(verbose_name='service area price')),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326, verbose_name='area')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_areas', to='providers.provider', verbose_name='provider')),
            ],
            options={
                'verbose_name': 'service area',
                'verbose_name_plural': 'service areas',
            },
        ),
    ]
