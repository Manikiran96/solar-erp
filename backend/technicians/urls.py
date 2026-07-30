from django.urls import (
    path,
    include
)

from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    TechnicianViewSet,
    WorkOrderViewSet
)

router = DefaultRouter()

router.register(
    "technicians",
    TechnicianViewSet,
    basename="technicians"
)

router.register(
    "workorders",
    WorkOrderViewSet,
    basename="workorders"
)

urlpatterns = [
    path(
        "",
        include(router.urls)
    )
]
