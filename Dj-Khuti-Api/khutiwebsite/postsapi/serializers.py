from rest_framework import serializers
from .models import PostsModel


class PostsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostsModel
        fields = [
            "id",
            "title",
            "description",
            "author",
            "created_at",
            "updated_at",
            "image",
            "post_detail",
        ]

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     if instance.image:
    #         representation["image"] = instance.image.name
    #     return representation

    post_detail = serializers.HyperlinkedIdentityField(
        view_name="postsapi:post", lookup_field="pk"
    )
