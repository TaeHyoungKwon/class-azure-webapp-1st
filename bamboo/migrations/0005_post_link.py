# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bamboo', '0004_delete_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
