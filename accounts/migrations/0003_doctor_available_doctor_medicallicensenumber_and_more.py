# Generated by Django 5.0.4 on 2024-04-27 11:04

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20240327_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='medicalLicenseNumber',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='subspeciality',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='workplace',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='dateOfDeath',
            field=models.DateField(default=datetime.datetime(2024, 4, 27, 17, 4, 56, 273155)),
        ),
        migrations.AddField(
            model_name='patient',
            name='nationality',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dateOfBirth',
            field=models.DateField(default=datetime.datetime(2024, 4, 27, 17, 4, 56, 273155)),
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workDay', models.CharField(max_length=10)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor')),
            ],
        ),
    ]
