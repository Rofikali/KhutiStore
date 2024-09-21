from rest_framework import serializers
from .models import Product, Category, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    # category_detail_url = serializers.HyperlinkedIdentityField(
    #     view_name="ecommerceshop:category-detail"
    # )

    class Meta:
        model = Category
        # fields = "__all__"
        fields = ["id", "name", "slug", "parent"]


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()

    product_detail_url = serializers.HyperlinkedIdentityField(
        view_name="ecommerceshop:products-detail",  # detail is by default is added
        # lookup_field="pk",
    )

    product_category_url = serializers.HyperlinkedIdentityField(
        view_name="ecommerceshop:product-category-list", lookup_field="category"
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "brand",
            "category",
            "product_detail_url",
            "product_category_url",
            "image",
        ]
        readonly = True
        editaboe = False

        # depth = 2


# class PostsModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostsModel
#         fields = [
#             "id",
#             "title",
#             "description",
#             "author",
#             "created_at",
#             "updated_at",
#             "image",
#             "post_detail",
#         ]

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         if instance.image:
#             representation["image"] = instance.image.name
#         return representation

#     post_detail = serializers.HyperlinkedIdentityField(
#         view_name="postsapi:post", lookup_field="pk"
# )
