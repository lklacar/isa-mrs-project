# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bartender',
            name='password_change_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='chef',
            name='password_change_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='waiter',
            name='password_change_count',
            field=models.IntegerField(default=0),
        ),
    ]
