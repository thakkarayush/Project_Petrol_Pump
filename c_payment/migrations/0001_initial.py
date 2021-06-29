# Generated by Django 3.2.3 on 2021-06-29 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creditor', '0003_auto_20210625_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='c_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('type', models.CharField(choices=[('paytm', 'paytm'), ('googlepay', 'googlepay'), ('bank', 'bank'), ('phonepay', 'phonepay')], max_length=20)),
                ('bankname', models.CharField(blank=True, max_length=20, null=True)),
                ('chequeno', models.IntegerField(blank=True, null=True)),
                ('branchname', models.CharField(blank=True, max_length=20, null=True)),
                ('check_date', models.DateField(blank=True, null=True)),
                ('reference_id', models.CharField(blank=True, max_length=20, null=True)),
                ('creditorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='creditor.creditor_master')),
            ],
        ),
    ]