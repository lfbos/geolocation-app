# Generated by Django 3.2.9 on 2021-11-15 00:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polygons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicearea',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='service area price'),
        ),
    ]
