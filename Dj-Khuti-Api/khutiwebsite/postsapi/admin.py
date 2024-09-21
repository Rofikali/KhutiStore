from django.contrib import admin
from .models import PostsModel


# Register your models here.
@admin.register(PostsModel)
class PostsModelAdmin(admin.ModelAdmin):
    # pass
    # list_display = ("__str__", "title", "description", "author")
    list_display = ("id", "title", "description", "author")
    # fields = [("slug", "title"), "description"]
    # list_display = ["title"]
    prepopulated_fields = {"slug": ["title"]}
