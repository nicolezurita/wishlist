# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish_app', '0003_auto_20170330_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywishlist',
            name='owner',
            field=models.CharField(default='', max_length=45),
        ),
    ]