# Generated by Django 4.0.6 on 2022-07-12 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_status_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='application',
            field=models.ForeignKey(default=100, on_delete=django.db.models.deletion.CASCADE, to='main_app.application'),
            preserve_default=False,
        ),
    ]
