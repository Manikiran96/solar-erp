from rest_framework import viewsets

from .models import (
    InventoryItem,
    MaterialIssue
)

from .serializers import (
    InventoryItemSerializer,
    MaterialIssueSerializer
)


class InventoryItemViewSet(viewsets.ModelViewSet):

    queryset = (
        InventoryItem.objects
        .all()
        .order_by("-id")
    )

    serializer_class = (
        InventoryItemSerializer
    )


class MaterialIssueViewSet(viewsets.ModelViewSet):

    queryset = (
        MaterialIssue.objects
        .all()
        .order_by("-id")
    )

    serializer_class = (
        MaterialIssueSerializer
    )
