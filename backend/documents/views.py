from rest_framework import viewsets

from .models import CustomerDocument
from .serializers import (
    CustomerDocumentSerializer
)


class CustomerDocumentViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        CustomerDocument.objects
        .all()
        .order_by("-id")
    )

    serializer_class = (
        CustomerDocumentSerializer
    )
