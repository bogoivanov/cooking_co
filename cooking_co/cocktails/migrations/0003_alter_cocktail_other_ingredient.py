# Generated by Django 4.1.2 on 2022-12-13 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0002_alter_cocktail_other_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='other_ingredient',
            field=models.CharField(max_length=150),
        ),
    ]