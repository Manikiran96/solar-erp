from rest_framework import viewsets

from .models import (
    CustomerPayment,
    Invoice
)

from .serializers import (
    CustomerPaymentSerializer,
    InvoiceSerializer
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
