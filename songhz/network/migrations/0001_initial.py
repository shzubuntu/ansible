# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-01 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=36)),
                ('status', models.CharField(max_length=10)),
                ('comment', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
            ],
        ),
    ]
