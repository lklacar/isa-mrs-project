# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='SingleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SingleDrinkOrder',
            fields=[
                ('singleorder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='order.SingleOrder')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Drink')),
            ],
            bases=('order.singleorder',),
        ),
        migrations.CreateModel(
            name='SingleFoodOrder',
            fields=[
                ('singleorder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='order.SingleOrder')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Food')),
            ],
            bases=('order.singleorder',),
        ),
        migrations.AddField(
            model_name='singleorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order'),
        ),
    ]