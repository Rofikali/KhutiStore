from .views import PostsListAPIView, PostsRetrieveAPIView
from django.urls import path

app_name = "postsapi"

urlpatterns = [
    path("posts", PostsListAPIView.as_view(), name="posts"),
    path("posts/<int:pk>", PostsRetrieveAPIView.as_view(), name="post"),
]

