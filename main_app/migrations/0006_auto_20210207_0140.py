# Generated by Django 3.1.6 on 2021-02-07 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210206_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fav_movies',
            field=models.ManyToManyField(to='main_app.Movie'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='subbed_services',
            field=models.ManyToManyField(to='main_app.Service'),
        ),
    ]
