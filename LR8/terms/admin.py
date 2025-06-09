from django.contrib import admin
from .models import Tag, Termite

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Termite)
class TermiteAdmin(admin.ModelAdmin):
    list_display = ('term', 'user', 'created_at')
    list_filter = ('tags', 'created_at')
    search_fields = ('term', 'definition')
    filter_horizontal = ('tags',)