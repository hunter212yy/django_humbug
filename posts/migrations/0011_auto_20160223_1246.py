# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20160222_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default="<img src='http://shere.buruma.net/wp-content/uploads/2014/09/django.png'>", upload_to='documents/%Y/%m/%d'),
        ),
    ]