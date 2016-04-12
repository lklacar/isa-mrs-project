# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[(b'GUEST', b'Guest'), (b'MANAGER', b'Manager'), (b'SYSTEM_MANAGER', b'System manager'), (b'WAITER', b'Waiter'), (b'CHEF', b'Chef'), (b'BARTENDER', b'Bartender')], default=b'GUEST', max_length=10),
        ),
    ]
