# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-06-02 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0011_auto_20180602_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='workfolwstep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folw', models.CharField(blank=True, max_length=10, null=True, verbose_name='流程名称')),
                ('code', models.CharField(blank=True, max_length=50, null=True, verbose_name='步骤编号')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='步骤名称')),
                ('approval', models.CharField(blank=True, max_length=10, null=True, verbose_name='是否审批')),
                ('skip', models.CharField(blank=True, max_length=10, null=True, verbose_name='能否跳过')),
                ('group', models.CharField(blank=True, max_length=50, null=True, verbose_name='角色')),
            ],
        ),
    ]
