# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_pokemon_qr_code_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='qr_code_image',
            field=models.ImageField(blank=True, null=True, upload_to='main/static/qr'),
        ),
    ]