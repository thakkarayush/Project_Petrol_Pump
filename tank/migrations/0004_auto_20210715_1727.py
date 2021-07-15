# Generated by Django 3.2.3 on 2021-07-15 11:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0003_alter_tank_master_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tank_master',
            name='oilcloseinlit',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
        migrations.AddField(
            model_name='tank_master',
            name='oilopeninlit',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
    ]
