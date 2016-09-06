# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mbella', '0006_auto_20160905_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dogum_tarihi',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mbella.User'),
        ),
    ]
