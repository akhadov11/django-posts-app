from django.contrib import admin

from main.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "body", "author", "published_on")
    list_display_links = ("id", "title")
    list_filter = ("published_on",)
    search_fields = ("title", "body")
