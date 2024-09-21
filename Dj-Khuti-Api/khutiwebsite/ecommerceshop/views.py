from .serializers import ProductSerializer, BrandSerializer, CategorySerializer
from .models import Product, Category, Brand

from rest_framework.pagination import LimitOffsetPagination  # type: ignore
from rest_framework.response import Response  # type: ignore
from django.shortcuts import get_object_or_404  # type: ignore

from rest_framework import viewsets, mixins  # type: ignore
from rest_framework.decorators import action  # type: ignore


class CustomPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 15


class BrandView(viewsets.ViewSet):
    """
    A simple ViewSet for listing all products.
    """

    queryset = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class CategoryView(viewsets.ViewSet):
    """
    A simple ViewSet for listing all products.
    """

    # def get_queryset(self):
    #     return Category.objects.all()

    queryset = Category.objects.all()

    def list(self, request):
        paginator = LimitOffsetPagination()
        paginator.default_limit = 5
        paginator_queryset = paginator.paginate_queryset(self.queryset, request)

        serializer = CategorySerializer(paginator_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        singe_data = get_object_or_404(self.queryset, pk=pk)
        serializer = CategorySerializer(singe_data)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     singe_data = get_object_or_404(self.queryset, pk=pk)
    #     serializer = CategorySerializer(singe_data, context={"request": request})
    #     return Response(serializer.data)


class ProductViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    A simple ViewSet for listing all products and a single product.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk"


class ProductByCategoryViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    A simple ViewSet for listing all products categories.
    """

    queryset = Product.objects.all()
    # serializer_class = ProductSerializer
    lookup_field = "category"
    pagination_class = LimitOffsetPagination

    def list(self, request, category=None):
        queryset = Product.objects.filter(category__name=category)
        serializer = ProductSerializer(
            queryset, context={"request": request}, many=True
        )
        return Response(serializer.data)


'''
# class ProductView(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing all products.
#     """

#     queryset = Product.objects.all()
#     # Lookup_fields = "name"

#     """
#     # def list(self, request):
#     #     # Set up pagination
#     #     paginator = PageNumberPagination()
#     #     paginator.page_size = 3

#     #     # Apply pagination to the queryset
#     #     paginated_queryset = paginator.paginate_queryset(self.queryset, request)

#     #     # Serialize the paginated data
#     #     serializer = ProductSerializer(paginated_queryset, many=True)
#     #     # return Response(serializer.data)
#     #     # Return the paginated response
#     #     return paginator.get_paginated_response(serializer.data)
#     """

#     def list(self, request):
#         # Set up pagination
#         paginator = CustomPagination()
#         # Apply pagination to the queryset
#         paginated_queryset = paginator.paginate_queryset(self.queryset, request)
#         print("request ", request)
#         # Serialize the paginated data
#         serializer = ProductSerializer(
#             paginated_queryset, many=True, context={"request": request}
#         )
#         return paginator.get_paginated_response(serializer.data)

#     def retrieve(self, request, pk=None):
#         singe_data = get_object_or_404(self.queryset, pk=pk)
#         serializer = ProductSerializer(singe_data, context={"request": request})
#         return Response(serializer.data)
'''
"""
# class ProductByCategoryViewSet(
#     # mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     viewsets.GenericViewSet,
# ):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = "category"

#     # Lookup_field = "category"

#     # def list(self, request):
#     #     paginator = CustomPagination()
#     #     paginated_queryset = paginator.paginate_queryset(self.queryset, request)
#     #     serializer = ProductSerializer(
#     #         paginated_queryset, many=True, context={"request": request}
#     #     )
#     #     return paginator.get_paginated_response(serializer.data)

#     # def list(self, request):
#     #     # Set up pagination
#     #     paginator = CustomPagination()
#     #     # Apply pagination to the queryset
#     #     paginated_queryset = paginator.paginate_queryset(self.queryset, request)
#     #     print("request ", request)
#     #     # Serialize the paginated data
#     #     serializer = ProductSerializer(
#     #         paginated_queryset, many=True, context={"request": request}
#     #     )
#     #     return paginator.get_paginated_response(serializer.data)

#     # def retrieve(self, request, pk=None):
#     #     singe_data = get_object_or_404(self.queryset, pk=pk)
#     #     serializer = ProductSerializer(singe_data, context={"request": request})
#     #     return Response(serializer.data)

#     @action(detail=False, url_path="(?P<category>[^/.]+)")
#     def by_category(self, request, category=None):
#         queryset = Product.objects.filter(category__name=category)
#         serializer = ProductSerializer(
#             queryset, many=True, context={"request": request}
#         )
#         return Response(serializer.data)

"""
'''
# class ProductByCategoryViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing all products categories.
#     """

#     queryset = Product.objects.all()

#     # Set up pagination
#     def list(self, request):
#         paginator = CustomPagination()
#         # queryset = Product.objects.all()
#         # Apply pagination to the queryset
#         paginated_queryset = paginator.paginate_queryset(self.queryset, request)
#         print("request ", request)
#         # Serialize the paginated data
#         serializer = ProductSerializer(
#             paginated_queryset, many=True, context={"request": request}
#         )
#         return paginator.get_paginated_response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Product.objects.filter(category__name=pk)
#         serializer = ProductSerializer(
#             queryset, many=True, context={"request": request}
#         )
#         return Response(serializer.data)

'''
