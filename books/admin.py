from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['author', 'story_name']
    search_fields = ['author', 'story_name']
