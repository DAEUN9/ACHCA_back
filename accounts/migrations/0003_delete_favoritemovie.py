# Generated by Django 3.2 on 2022-05-19 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FavoriteMovie',
        ),
    ]