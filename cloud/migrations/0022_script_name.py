# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-07-24 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0021_step_pnode'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='name',
            field=models.CharField(blank=True, max_length=500, verbose_name='脚本名称'),
        ),
    ]
