# Generated by Django 4.0.6 on 2022-07-12 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_contact_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='notes',
            field=models.TextField(max_length=115),
        ),
    ]
