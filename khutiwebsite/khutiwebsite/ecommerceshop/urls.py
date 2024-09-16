from .views import (
    BrandView,
    CategoryView,
    ProductByCategoryViewSet,
    ProductViewSet,
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = "ecommerceshop"

router = DefaultRouter()
router.register(r"api/brands", BrandView, basename="brand")
router.register(r"api/categories", CategoryView, basename="category")

router.register(
    r"api/porducts",
    ProductViewSet,
    basename="products",
)

# (?P<category>[^/.]+)
router.register(
    r"api/porducts_by_category/(?P<category>[^/.]+)",
    ProductByCategoryViewSet,
    basename="product-category",
)

urlpatterns = [
    path("", include(router.urls)),
]
