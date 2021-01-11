# Generated by Django 3.0 on 2021-01-11 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_movie_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('action', 'ACTION'), ('drama', 'DRAMA'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE'), ('horror', 'HORROR')], max_length=10),
        ),
    ]
