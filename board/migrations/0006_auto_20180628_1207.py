# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20180628_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addboard',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
