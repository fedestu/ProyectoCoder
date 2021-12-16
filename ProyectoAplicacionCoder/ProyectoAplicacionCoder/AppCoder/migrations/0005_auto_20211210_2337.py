# Generated by Django 3.2.9 on 2021-12-11 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_auto_20211209_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='esNoche',
            field=models.BooleanField(null=True),
        ),
    ]