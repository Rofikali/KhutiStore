from django.contrib import admin
from .models import Product, Category, Brand


@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    # pass
    # list_display = ("__str__", "title", "description", "author")
    list_display = (
        "id",
        "name",
    )


# Register your models here.
@admin.register(Category)
class PostsModelAdmin(admin.ModelAdmin):
    # pass
    # list_display = ("__str__", "title", "description", "author")
    list_display = (
        "id",
        "name",
    )
    # fields = [("slug", "title"), "description"]
    # list_display = ["title"]
    prepopulated_fields = {"slug": ["name"]}
    # prepopulated_fields = {"name": ["slug"]}


# Register your models here.
@admin.register(Product)
class PostsModelAdmin(admin.ModelAdmin):
    # pass
    # list_display = ("__str__", "title", "description", "author")
    list_display = ("id", "name", "description",'category')
    # fields = [("slug", "title"), "description"]
    # list_display = ["title"]
    # prepopulated_fields = {"slug": ["title"]}
