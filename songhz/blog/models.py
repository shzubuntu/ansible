# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Create your models here.
class User(models.Model):
    UserName=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)

class Host(models.Model):
    hostname=models.CharField(max_length=200)
    ip=models.CharField(max_length=36)

class Ip(models.Model):
    ip=models.CharField(max_length=36)
    status=models.CharField(max_length=10)
    comment=models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True)