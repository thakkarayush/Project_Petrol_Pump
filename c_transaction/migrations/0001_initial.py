# Generated by Django 3.2.3 on 2021-06-29 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '0001_initial'),
        ('nozzel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='c_transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('petrolinlit', models.FloatField(blank=True, null=True)),
                ('dieselinlit', models.FloatField(blank=True, null=True)),
                ('petrolprice', models.FloatField(blank=True, null=True)),
                ('dieselprice', models.FloatField(blank=True, null=True)),
                ('nozzle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ctransaction', to='nozzel.nozzel_master')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ctransaction', to='vehicle.vehicle')),
            ],
        ),
    ]
