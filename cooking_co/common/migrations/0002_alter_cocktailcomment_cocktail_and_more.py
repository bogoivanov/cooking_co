# Generated by Django 4.1.4 on 2022-12-21 17:12

import cooking_co.common.core.dirty_words_validator
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0004_alter_cocktail_cocktail_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_alter_recipe_recipe_photo'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktailcomment',
            name='cocktail',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cocktails.cocktail'),
        ),
        migrations.AlterField(
            model_name='cocktailcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cocktaillike',
            name='cocktail',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cocktails.cocktail'),
        ),
        migrations.AlterField(
            model_name='cocktaillike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipecomment',
            name='recipe',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe'),
        ),
        migrations.AlterField(
            model_name='recipecomment',
            name='text',
            field=models.CharField(max_length=300, validators=[cooking_co.common.core.dirty_words_validator.validate_dirty_words]),
        ),
        migrations.AlterField(
            model_name='recipecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipelike',
            name='recipe',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe'),
        ),
        migrations.AlterField(
            model_name='recipelike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
