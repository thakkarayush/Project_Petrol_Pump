# Generated by Django 3.2.3 on 2021-06-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_payment',
            name='chequeno',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
