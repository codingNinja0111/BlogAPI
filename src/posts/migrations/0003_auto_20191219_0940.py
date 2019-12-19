# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-19 09:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 9, 40, 37, 640257, tzinfo=utc)),
            preserve_default=False,
        ),
    ]