from rest_framework import viewsets

from .models import (
    CustomerPayment,
    Invoice
)

from .serializers import (
    CustomerPaymentSerializer,
    InvoiceSerializer
)
from rest_framework.permissions import (
    IsAuthenticated
)

class CustomerPaymentViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        CustomerPayment.objects
        .all()
        .order_by("-id")
    )

    serializer_class = (
        CustomerPaymentSerializer
    )
    permission_classes = [IsAuthenticated]

class InvoiceViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Invoice.objects
        .all()
        .order_by("-id")
    )

    serializer_class = (
        InvoiceSerializer
    )
    permission_classes = [IsAuthenticated]
