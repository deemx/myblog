# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150820_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=35)),
                ('comment', models.TextField(default='')),
                ('post', models.ForeignKey(to='app.Post')),
            ],
        ),
        migrations.RemoveField(
            model_name='commentform',
            name='post',
        ),
        migrations.DeleteModel(
            name='CommentForm',
        ),
    ]
