# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import ProjectInfo


@admin.register(ProjectInfo)
class HookerAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary', 'is_active')
