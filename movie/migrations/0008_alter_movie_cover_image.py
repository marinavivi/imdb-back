# Generated by Django 4.0.4 on 2022-05-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_alter_movie_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover_image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
