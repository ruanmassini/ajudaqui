# Generated by Django 4.0.6 on 2022-09-19 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='autor',
            new_name='title',
        ),
    ]