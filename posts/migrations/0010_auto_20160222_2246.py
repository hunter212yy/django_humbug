# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default="<img src='http://shere.buruma.net/wp-content/uploads/2014/09/django.png'>", upload_to=''),
        ),
    ]