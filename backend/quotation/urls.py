from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .pdf_views import quotation_pdf
from .views import (
    PricingRuleViewSet,
    QuotationViewSet
)

router = DefaultRouter()

router.register(
    "pricing-rules",
    PricingRuleViewSet
)

router.register(
    "quotations",
    QuotationViewSet
)

urlpatterns = [
    path("", include(router.urls)),
    path(
    "quotation-pdf/<int:pk>/",
    quotation_pdf
)
]
