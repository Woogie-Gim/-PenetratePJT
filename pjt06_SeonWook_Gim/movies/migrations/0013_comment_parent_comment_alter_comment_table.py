# Generated by Django 4.2.2 on 2023-10-19 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_movie_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.comment'),
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
    ]