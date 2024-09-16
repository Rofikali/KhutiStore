from rest_framework.generics import ListAPIView, RetrieveAPIView

# from rest_framework.pagination import LimitOffsetPagination

from .models import PostsModel
from .serializers import PostsModelSerializer


class PostsListAPIView(ListAPIView):
    queryset = PostsModel.objects.all()
    serializer_class = PostsModelSerializer

    # pagination_class = LimitOffsetPagination


class PostsRetrieveAPIView(RetrieveAPIView):
    queryset = PostsModel.objects.all()
    serializer_class = PostsModelSerializer
