# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-22 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0015_auto_20181122_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cuisines',
            field=models.CharField(blank=True, default=None, max_length=264),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(blank=True, default=None, max_length=264),
        ),
    ]
