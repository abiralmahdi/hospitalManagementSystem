# Generated by Django 5.0.4 on 2024-04-27 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_patient_dateofbirth_alter_patient_dateofdeath_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='dateOfBirth',
            field=models.DateField(default=datetime.datetime(2024, 4, 27, 18, 9, 48, 219396)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dateOfDeath',
            field=models.DateField(default=datetime.datetime(2024, 4, 27, 18, 9, 48, 219396), null=True),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
