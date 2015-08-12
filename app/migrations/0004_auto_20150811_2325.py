# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150805_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='posts',
            new_name='tags',
        ),
    ]
