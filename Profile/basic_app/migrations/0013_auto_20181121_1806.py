# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-21 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0012_auto_20181121_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
