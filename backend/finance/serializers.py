from rest_framework import serializers

from .models import (
    CustomerPayment,
    Invoice
)


class CustomerPaymentSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = CustomerPayment
        fields = "__all__"


class InvoiceSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Invoice
        fields = "__all__"
