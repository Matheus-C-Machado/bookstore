from rest_framework import routers
from django.urls import path, include
from order.viewsets import OrderViewSet

router = routers.SimpleRouter()
router.register(r"", OrderViewSet, basename="order")  # "" vazio funciona

urlpatterns = [
    path("", include(router.urls)),
]