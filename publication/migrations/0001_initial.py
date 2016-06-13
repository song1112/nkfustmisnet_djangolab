# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-12 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='\u6c92\u6709\u540d', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('topic', models.CharField(default='\u7121\u984c', max_length=20)),
                ('message', models.TextField(default='\u7121\u5167\u5bb9')),
            ],
        ),
    ]
