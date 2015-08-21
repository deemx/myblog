# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_commentfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentForm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('post', models.ForeignKey(to='app.Post')),
            ],
        ),
        migrations.DeleteModel(
            name='CommentField',
        ),
    ]
