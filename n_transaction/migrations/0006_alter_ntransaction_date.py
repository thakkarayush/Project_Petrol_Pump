# Generated by Django 3.2.3 on 2021-07-15 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n_transaction', '0005_auto_20210711_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ntransaction',
            name='date',
            field=models.DateField(default=datetime.datetime.utcnow),
        ),
    ]
