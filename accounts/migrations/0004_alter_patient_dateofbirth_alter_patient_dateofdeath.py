# Generated by Django 5.0.4 on 2024-04-27 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_doctor_available_doctor_medicallicensenumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='dateOfBirth',
            field=models.DateField(default=datetime.datetime(2024, 4, 27, 17, 56, 53, 663716)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dateOfDeath',
            field=models.DateField(default=datetime.datetime(2024, 4, 27, 17, 56, 53, 663716), null=True),
        ),
    ]
