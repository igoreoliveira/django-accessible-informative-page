from django.contrib import admin
from . import models


class BlockInline(admin.StackedInline):
    model = models.Block
    ordering = ['order']


@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    inlines = [BlockInline]



# Register your models here.
