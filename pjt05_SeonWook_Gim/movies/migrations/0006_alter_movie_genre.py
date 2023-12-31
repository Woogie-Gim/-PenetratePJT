# Generated by Django 4.2.5 on 2023-10-13 04:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('CM', 'Comedy'), ('FN', 'Fantansy'), ('RM', 'Romanace')], default='Comedy', max_length=100, null='CM', validators=[django.core.validators.MinValueValidator(0, 5), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
