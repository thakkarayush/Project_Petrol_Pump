# Generated by Django 3.2.3 on 2021-06-21 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210620_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='shifttime',
            field=models.DateTimeField(choices=[('Morning', 'Morning'), ('Noon', 'Noon'), ('Night', 'Night')]),
        ),
    ]
