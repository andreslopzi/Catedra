# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-08 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0006_auto_20180608_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='correo',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
