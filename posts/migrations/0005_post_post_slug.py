# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20160217_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_slug',
            field=models.SlugField(default='sas-quatch'),
            preserve_default=False,
        ),
    ]
