# Generated by Django 4.0.6 on 2022-07-12 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_remove_status_application_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
    ]