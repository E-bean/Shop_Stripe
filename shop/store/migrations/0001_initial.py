# Generated by Django 3.2.16 on 2022-11-21 09:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Product Name')),
                ('description', models.TextField(verbose_name='Product description')),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(100)], verbose_name='Product price in cents')),
            ],
        ),
    ]