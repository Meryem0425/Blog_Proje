# Generated by Django 5.0.1 on 2024-03-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arama',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]