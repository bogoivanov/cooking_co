# Generated by Django 4.1.2 on 2022-12-09 18:20

import cooking_co.cocktails.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cocktail_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('cocktail_photo', models.URLField(blank=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('main_ingredient', models.CharField(blank=True, choices=[('non-alcoholic', 'non-alcoholic'), ('vodka', 'vodka'), ('whiskey', 'whiskey'), ('liquors', 'liquors'), ('rum', 'rum'), ('gin', 'gin'), ('tequila', 'tequila')], default='non-alcoholic', max_length=30)),
                ('other_ingredient', models.CharField(max_length=30)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['cocktail_name'],
            },
            bases=(cooking_co.cocktails.models.StrFromFieldsMixin, models.Model),
        ),
    ]
