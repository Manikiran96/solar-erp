from rest_framework import serializers
from .models import CustomerDocument


class CustomerDocumentSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = CustomerDocument
        fields = "__all__"
