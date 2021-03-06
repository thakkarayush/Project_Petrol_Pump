# Generated by Django 3.2.3 on 2021-07-14 10:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_employee_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='IFSCcode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10, 'Phone numer must be of 10 digit')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='telephone',
            field=models.CharField(max_length=7, validators=[django.core.validators.MinLengthValidator(7, 'Phone numer must be of 7 digit')]),
        ),
    ]
