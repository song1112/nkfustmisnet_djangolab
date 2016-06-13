# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=20, default="沒有名")
    email = models.EmailField()
    phone = models.CharField(blank=True, null=True, max_length=20)

class Subject(models.Model):
    uid =  models.IntegerField()
    topic = models.CharField(max_length=20, default="無題")
    message = models.TextField(default="無內容")
