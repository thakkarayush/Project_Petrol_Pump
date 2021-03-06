# Generated by Django 3.2.3 on 2021-07-15 09:50

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0002_auto_20210625_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='oil_rate',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rate',
            name='date',
            field=models.DateField(default=datetime.datetime.utcnow),
        ),
    ]
