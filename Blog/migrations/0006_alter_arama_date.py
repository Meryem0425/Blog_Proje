# Generated by Django 5.0.1 on 2024-03-21 08:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_alter_arama_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arama',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]