# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 17:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_message', models.TextField()),
                ('comment_created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poongchang_comments_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('hit', models.IntegerField(blank=True, default=0, null=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poongchang_post_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poongchang_comments', to='poongchang.Post'),
        ),
    ]
