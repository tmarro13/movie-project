# Generated by Django 4.2.16 on 2024-12-04 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "project",
            "0004_movie_tmdb_id_alter_movie_director_alter_movie_image_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="review", old_name="date", new_name="created_at",
        ),
    ]
