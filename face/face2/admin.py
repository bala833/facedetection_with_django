# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Videos, Face


@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'video')


@admin.register(Face)
class FaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
