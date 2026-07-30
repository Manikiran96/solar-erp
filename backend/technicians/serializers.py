from rest_framework import serializers

from .models import (
    Technician,
    WorkOrder
)


class TechnicianSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Technician
        fields = "__all__"


class WorkOrderSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = WorkOrder
        fields = "__all__"
