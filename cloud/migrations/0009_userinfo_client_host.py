# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-06-02 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0008_auto_20180531_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='client_host',
            field=models.ManyToManyField(to='cloud.ClientHost'),
        ),
    ]
