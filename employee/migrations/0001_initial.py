# Generated by Django 3.2.3 on 2021-06-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('telephone', models.IntegerField()),
                ('block', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=10)),
                ('pin', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('education', models.CharField(max_length=10)),
                ('dateofjoin', models.DateField()),
                ('shifttime', models.DateTimeField()),
                ('workinghours', models.DateTimeField()),
                ('salary', models.IntegerField()),
                ('bankname', models.CharField(max_length=30)),
                ('bankaccountno', models.IntegerField()),
                ('IFSCcode', models.IntegerField()),
                ('panno', models.IntegerField()),
                ('aadharno', models.IntegerField()),
                ('reference', models.CharField(max_length=10)),
                ('photo', models.ImageField(upload_to='')),
                ('document', models.FileField(upload_to='')),
            ],
        ),
    ]
