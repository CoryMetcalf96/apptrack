# Generated by Django 4.0.6 on 2022-07-11 19:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_application_date_applied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='date_applied',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
