# Generated by Django 3.2.3 on 2021-07-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplierdetail', '0002_alter_supplierdetails_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierdetails',
            name='oilinlit',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
