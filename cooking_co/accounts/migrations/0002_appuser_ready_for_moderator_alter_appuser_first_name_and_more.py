# Generated by Django 4.1.2 on 2022-12-14 15:46

import cooking_co.accounts.validators.validate_only_letters
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='ready_for_moderator',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), cooking_co.accounts.validators.validate_only_letters.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), cooking_co.accounts.validators.validate_only_letters.validate_only_letters]),
        ),
    ]
