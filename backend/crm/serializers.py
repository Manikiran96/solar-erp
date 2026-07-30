from rest_framework import serializers
from .models import Lead, LeadFollowUp


class LeadFollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadFollowUp
        fields = "__all__"


class LeadSerializer(serializers.ModelSerializer):
    followups = LeadFollowUpSerializer(many=True, read_only=True)

    class Meta:
        model = Lead
        fields = "__all__"
        read_only_fields = ["lead_id", "created_at", "updated_at"]


class LeadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = [
            "id",
            "lead_id",
            "customer_name",
            "mobile",
            "location",
            "customer_category",
            "project_type",
            "expected_capacity",
            "estimated_cost",
            "lead_source",
            "status",
            "assigned_to",
            "created_at",
        ]
