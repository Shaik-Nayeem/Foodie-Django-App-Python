# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-22 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0016_auto_20181122_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='document',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
