# Generated by Django 3.2.3 on 2021-07-20 12:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n_transaction', '0007_alter_ntransaction_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ntransaction',
            name='amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='card',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='cash',
            field=models.CharField(blank=True, default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='closinglitdiesel',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='closinglitpetrol',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='creditoramount',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='googlepay',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='lostdiesel',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='lostdieselprice',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='lostpetrol',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='lostpetrolprice',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='openinglitdiesel',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='openinglitpetrol',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='paytm',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='phonepay',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='totaldiesel',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='totaldprice',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='totalpetrol',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='totalpprice',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
    ]
