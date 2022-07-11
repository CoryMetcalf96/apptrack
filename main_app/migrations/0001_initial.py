# Generated by Django 4.0.6 on 2022-07-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_website', models.CharField(max_length=200)),
                ('company_summary', models.TextField(max_length=1000)),
                ('application_link', models.CharField(max_length=200)),
                ('notes', models.TextField(max_length=1000)),
            ],
        ),
    ]
