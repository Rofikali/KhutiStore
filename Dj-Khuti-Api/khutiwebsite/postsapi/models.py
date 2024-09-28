from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

Author = User


class PostsModel(models.Model):
    title = models.CharField(max_length=100, editable=True)
    # description = models.TextField(editable=True)
    description = HTMLField()
    slug = models.CharField(max_length=100, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d/")

    author = models.ForeignKey(User, on_delete=models.Case, related_name="posts_author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
