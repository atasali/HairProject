# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-06 21:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mbella', '0017_auto_20160907_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='eklenme_tarihi',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 6, 21, 26, 31, 436162, tzinfo=utc)),
        ),
    ]
