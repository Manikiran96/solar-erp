from django.urls import (
    path,
    include
)

from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    CustomerDocumentViewSet
)

router = DefaultRouter()

router.register(
    "documents",
    CustomerDocumentViewSet,
    basename="documents"
)

urlpatterns = [
    path(
        "",
        include(router.urls)
    )
]
