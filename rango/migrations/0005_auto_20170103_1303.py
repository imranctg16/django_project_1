# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-03 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20170103_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='slug',
            field=models.SlugField(default='', verbose_name=''),
            preserve_default=False,
        ),
    ]
