# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150820_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentform',
            name='comment',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='commentform',
            name='nickname',
            field=models.CharField(max_length=35, default=datetime.datetime(2015, 8, 20, 21, 35, 32, 497383)),
            preserve_default=False,
        ),
    ]
