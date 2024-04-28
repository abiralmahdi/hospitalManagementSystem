# Generated by Django 5.0.4 on 2024-04-27 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_patient_dateofbirth_alter_patient_dateofdeath_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dateOfBirth',
            field=models.DateField(default=datetime.datetime(2024, 4, 28, 0, 17, 46, 704747)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dateOfDeath',
            field=models.DateField(default=datetime.datetime(2024, 4, 28, 0, 17, 46, 704747), null=True),
        ),
    ]