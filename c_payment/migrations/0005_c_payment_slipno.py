# Generated by Django 3.2.3 on 2021-07-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_payment', '0004_alter_c_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_payment',
            name='slipno',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
    ]
