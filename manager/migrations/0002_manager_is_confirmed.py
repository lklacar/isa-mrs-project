# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
