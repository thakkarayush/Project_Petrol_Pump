# Generated by Django 3.2.3 on 2021-06-10 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('petrol_price', models.FloatField()),
                ('diesel_price', models.FloatField()),
            ],
        ),
    ]
