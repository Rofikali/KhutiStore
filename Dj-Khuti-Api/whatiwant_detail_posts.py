# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import PostsModel
# from .serializers import PostsModelSerializer


# class CombinedPostsView(APIView):
#     def get(self, request, *args, **kwargs):
#         # Get all posts
#         all_posts = PostsModel.objects.all()
#         all_posts_serializer = PostsModelSerializer(
#             all_posts, many=True, context={"request": request}
#         )

#         # Get single post based on the first post (or customize as needed)
#         single_post_id = kwargs.get("pk", 1)  # Fallback to ID 1 if no pk is provided
#         try:
#             single_post = PostsModel.objects.get(id=single_post_id)
#             single_post_serializer = PostsModelSerializer(
#                 single_post, context={"request": request}
#             )
#         except PostsModel.DoesNotExist:
#             return Response(
#                 {"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND
#             )

#         return Response(
#             {
#                 "posts_list": all_posts_serializer.data,
#                 "post_detail": single_post_serializer.data,
#             }
#         )


# from rest_framework import serializers
# from .models import PostsModel

# # serializers


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
#     )
#     # )
#     #     view_name="postsapi:post", lookup_field="pk"
#     # )


# # urls 
# from .views import CombinedPostsView
# from django.urls import path

# app_name = "postsapi"

# urlpatterns = [
#     path("combined-posts/", CombinedPostsView.as_view(), name="combined-posts"),
#     path("posts/<int:pk>/", CombinedPostsView.as_view(), name="post"),
# ]
