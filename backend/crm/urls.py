from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    LeadViewSet,
    LeadFollowUpViewSet,
    ConvertedLeadViewSet,
    LostLeadViewSet
)


router = DefaultRouter()

router.register(
    "leads",
    LeadViewSet,
    basename="leads"
)

router.register(
    "followups",
    LeadFollowUpViewSet,
    basename="followups"
)

router.register(
    "converted-leads",
    ConvertedLeadViewSet,
    basename="converted-leads"
)

router.register(
    "lost-leads",
    LostLeadViewSet,
    basename="lost-leads"
)


urlpatterns = [
    path(
        "",
        include(router.urls)
    ),
]
