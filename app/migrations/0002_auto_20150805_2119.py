# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TagsAdmin',
            fields=[
                ('tags_ptr', models.OneToOneField(auto_created=True, serialize=False, to='app.Tags', primary_key=True, parent_link=True)),
            ],
            bases=('app.tags',),
        ),
        migrations.AddField(
            model_name='tags',
            name='posts',
            field=models.ManyToManyField(to='app.Post'),
        ),
    ]
