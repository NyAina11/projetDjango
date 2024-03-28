# Generated by Django 5.0.2 on 2024-03-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('studio', models.CharField(max_length=64, unique=True)),
                ('release_date', models.DateField(verbose_name='date released')),
            ],
        ),
    ]