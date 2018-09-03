# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    search_fields = ['title', 'author']

admin.site.register(Post, PostAdmin)