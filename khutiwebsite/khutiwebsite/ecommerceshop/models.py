from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

"""
# class Category(models.Model):
#     name = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.name


# class Product(models.Model):
#     name = models.CharField(max_length=100, blank=True, null=True)
#     description = models.TextField()
#     category = models.ForeignKey(Category, related_name="product_category", on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
"""


class Brand(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    slug = models.SlugField(max_length=100, unique=False) # check unique 
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey(
        Category, related_name="product_category", on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand, related_name="roduct_brand", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
