# Generated by Django 4.0.5 on 2022-07-19 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clapperboardApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juegos',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='musica',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='series',
            name='usuario',
        ),
    ]
