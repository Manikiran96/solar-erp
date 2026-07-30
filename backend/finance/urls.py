from django.urls import (
    path,
    include
)

from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    CustomerPaymentViewSet,
    InvoiceViewSet
)

router = DefaultRouter()

router.register(
    "payments",
    CustomerPaymentViewSet,
    basename="payments"
)

router.register(
    "invoices",
    InvoiceViewSet,
    basename="invoices"
)

urlpatterns = [
    path(
        "",
        include(router.urls)
    )
]
