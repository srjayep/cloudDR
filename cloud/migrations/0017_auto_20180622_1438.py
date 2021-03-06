# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-06-22 06:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0016_auto_20180622_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.DateTimeField(blank=True, null=True, verbose_name='开始时间')),
                ('endtime', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
                ('creatuser', models.CharField(blank=True, max_length=50, verbose_name='发起人')),
                ('state', models.CharField(blank=True, max_length=20, null=True, verbose_name='状态')),
                ('DataSet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloud.DataSet')),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloud.Process')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.DateTimeField(blank=True, null=True, verbose_name='发送时间')),
                ('senduser', models.CharField(blank=True, max_length=50, null=True, verbose_name='操作人')),
                ('receiveuser', models.CharField(blank=True, max_length=50, null=True, verbose_name='操作人')),
                ('receiveauth', models.CharField(blank=True, max_length=50, null=True, verbose_name='接收角色')),
                ('operator', models.CharField(blank=True, max_length=50, null=True, verbose_name='操作人')),
                ('endtime', models.DateTimeField(blank=True, null=True, verbose_name='处理时间')),
                ('type', models.CharField(blank=True, max_length=20, null=True, verbose_name='任务类型')),
                ('content', models.CharField(blank=True, max_length=5000, null=True, verbose_name='任务内容')),
                ('state', models.CharField(blank=True, max_length=20, null=True, verbose_name='状态')),
                ('result', models.CharField(blank=True, max_length=5000, null=True, verbose_name='处理结果')),
                ('explain', models.CharField(blank=True, max_length=5000, null=True, verbose_name='处理说明')),
                ('processrun', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud.ProcessRun')),
            ],
        ),
        migrations.CreateModel(
            name='ScriptRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.DateTimeField(blank=True, null=True, verbose_name='开始时间')),
                ('endtime', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
                ('operator', models.CharField(blank=True, max_length=50, null=True, verbose_name='操作人')),
                ('result', models.CharField(blank=True, max_length=5000, null=True, verbose_name='运行结果')),
                ('explain', models.CharField(blank=True, max_length=5000, null=True, verbose_name='运行说明')),
                ('runlog', models.CharField(blank=True, max_length=5000, null=True, verbose_name='运行日志')),
                ('state', models.CharField(blank=True, max_length=20, null=True, verbose_name='状态')),
                ('script', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud.Script')),
            ],
        ),
        migrations.CreateModel(
            name='StepRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.DateTimeField(blank=True, null=True, verbose_name='开始时间')),
                ('endtime', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
                ('operator', models.CharField(blank=True, max_length=50, null=True, verbose_name='操作人')),
                ('parameter', models.CharField(blank=True, max_length=5000, null=True, verbose_name='运行参数')),
                ('result', models.CharField(blank=True, max_length=5000, null=True, verbose_name='运行结果')),
                ('explain', models.CharField(blank=True, max_length=5000, null=True, verbose_name='运行说明')),
                ('state', models.CharField(blank=True, max_length=20, null=True, verbose_name='状态')),
                ('processrun', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud.ProcessRun')),
                ('step', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud.Step')),
            ],
        ),
        migrations.AddField(
            model_name='scriptrun',
            name='steprun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud.StepRun'),
        ),
        migrations.AddField(
            model_name='processtask',
            name='steprun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud.StepRun'),
        ),
    ]
