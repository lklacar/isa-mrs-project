# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 11:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_genericuser_is_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmationtoken',
            name='user',
        ),
    ]