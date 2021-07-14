# Generated by Django 3.2.3 on 2021-07-14 10:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditor', '0003_auto_20210625_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditor_master',
            name='contactpersonmobile',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10, 'Phone numer must be of 10 digit')]),
        ),
        migrations.AlterField(
            model_name='creditor_master',
            name='homeno',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(7, 'Phone numer must be of 7 digit')]),
        ),
        migrations.AlterField(
            model_name='creditor_master',
            name='officeno',
            field=models.CharField(max_length=7, validators=[django.core.validators.MinLengthValidator(7, 'Telephone numer must be of 7 digit')]),
        ),
        migrations.AlterField(
            model_name='creditor_master',
            name='pendingbalance',
            field=models.IntegerField(default=0),
        ),
    ]
