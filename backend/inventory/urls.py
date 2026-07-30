from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    InventoryItemViewSet,
    MaterialIssueViewSet
)

router = DefaultRouter()

router.register(
    "items",
    InventoryItemViewSet,
    basename="items"
)

router.register(
    "material-issues",
    MaterialIssueViewSet,
    basename="material-issues"
)

urlpatterns = [
    path(
        "",
        include(router.urls)
    )
]
