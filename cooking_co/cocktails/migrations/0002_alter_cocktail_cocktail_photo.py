# Generated by Django 4.1.2 on 2022-12-15 12:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='cocktail_photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
    ]