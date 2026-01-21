from django.contrib import admin
from blog.models import BlogPost


@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content_blog", "date_publication")
    list_filter = ("bool_blog",)
    search_fields = ("title",)
