# Generated by Django 3.2.9 on 2021-12-10 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_estadio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estadio',
            old_name='numero',
            new_name='anioFund',
        ),
        migrations.RenameField(
            model_name='estadio',
            old_name='apellido',
            new_name='direccion',
        ),
    ]
