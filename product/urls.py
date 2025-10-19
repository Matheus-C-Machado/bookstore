from django.urls import include, path
from rest_framework import routers
from product import viewsets

router = routers.SimpleRouter()
router.register(r"", viewsets.ProductViewSet, basename="product")  # ← vazio
router.register(r"category", viewsets.CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]