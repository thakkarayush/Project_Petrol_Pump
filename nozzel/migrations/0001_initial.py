# Generated by Django 3.2.3 on 2021-06-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nozzel_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nozzel_no', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('petrol', 'petrol'), ('diesel', 'diesel')], default='petrol', max_length=30)),
                ('remark', models.CharField(max_length=30)),
            ],
        ),
    ]
