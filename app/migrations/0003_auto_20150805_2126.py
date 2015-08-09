# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150805_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='tags',
            name='posts',
        ),
        migrations.RemoveField(
            model_name='tagsadmin',
            name='tags_ptr',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.DeleteModel(
            name='TagsAdmin',
        ),
        migrations.AddField(
            model_name='post',
            name='posts',
            field=models.ManyToManyField(to='app.Tag'),
        ),
    ]
