# Generated by Django 4.2.9 on 2024-05-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='studio',
            field=models.CharField(max_length=64),
        ),
    ]
