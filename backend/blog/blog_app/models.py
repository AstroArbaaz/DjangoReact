# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    tags = models.TextField(null=True, blank=True)
    article = models.TextField()
    author = models.ForeignKey(User)


    def __unicode__(self):
        return self.title