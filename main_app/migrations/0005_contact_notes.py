# Generated by Django 4.0.6 on 2022-07-12 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='notes',
            field=models.TextField(default='default', max_length=250),
            preserve_default=False,
        ),
    ]