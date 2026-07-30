from django.urls import (
    path,
    include
)

from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    LeadViewSet,
    LeadFollowUpViewSet
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

urlpatterns = [
    path(
        "",
        include(router.urls)
    )
]
