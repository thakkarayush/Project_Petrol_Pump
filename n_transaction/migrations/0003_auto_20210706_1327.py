# Generated by Django 3.2.3 on 2021-07-06 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n_transaction', '0002_auto_20210702_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ntransaction',
            old_name='dieselafter',
            new_name='card',
        ),
        migrations.RenameField(
            model_name='ntransaction',
            old_name='reference_id',
            new_name='cash',
        ),
        migrations.RenameField(
            model_name='ntransaction',
            old_name='dieselbefore',
            new_name='googlepay',
        ),
        migrations.RenameField(
            model_name='ntransaction',
            old_name='petrolbefore',
            new_name='paytm',
        ),
        migrations.RenameField(
            model_name='ntransaction',
            old_name='petrolafter',
            new_name='phonepay',
        ),
        migrations.RemoveField(
            model_name='ntransaction',
            name='type',
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='closingtime',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ntransaction',
            name='openingtime',
            field=models.FloatField(blank=True, null=True),
        ),
    ]