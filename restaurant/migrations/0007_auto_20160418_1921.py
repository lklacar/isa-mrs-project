# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_auto_20160418_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='profile_image',
            field=models.ImageField(upload_to=b''),
        ),
    ]
