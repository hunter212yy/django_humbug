# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20160217_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='posts.Tag'),
        ),
    ]
