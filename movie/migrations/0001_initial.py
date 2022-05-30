# Generated by Django 4.0.4 on 2022-05-25 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
                ('cover_image', models.CharField(max_length=60)),
                ('genre', models.CharField(choices=[('DRAMA', 'Drama'), ('ANIMATION', 'Animation'), ('HOROR', 'Horor'), ('DOCUMENTARY', 'Documentary'), ('UNDEFINED', 'Undefined')], default='UNDEFINED', max_length=30)),
            ],
        ),
    ]