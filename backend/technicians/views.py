from rest_framework import viewsets

from .models import (
    Technician,
    WorkOrder
)

from .serializers import (
    TechnicianSerializer,
    WorkOrderSerializer
)


class TechnicianViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Technician.objects
        .all()
        .order_by("-id")
    )

    serializer_class = (
        TechnicianSerializer
    )


class WorkOrderViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        WorkOrder.objects
        .all()
        .order_by("-id")
    )

    serializer_class = (
        WorkOrderSerializer
    )
