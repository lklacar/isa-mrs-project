# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemmanager',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
