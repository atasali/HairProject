# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbella', '0010_auto_20160905_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dogum_tarihi',
            field=models.DateField(blank=True, default=1),
        ),
    ]
