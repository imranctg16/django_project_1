# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-03 07:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20170103_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagory',
            name='slug',
        ),
    ]
