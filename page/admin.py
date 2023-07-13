from django.contrib import admin
from . import models


admin.site.register(models.Block)
class BlockInline(admin.TabularInline):
    model = models.Block


@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    inlines = [BlockInline]



# Register your models here.
