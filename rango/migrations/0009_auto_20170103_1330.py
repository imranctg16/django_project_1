# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-03 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0008_auto_20170103_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
