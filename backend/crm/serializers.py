from rest_framework import serializers

from .models import (
    Lead,
    LeadFollowUp
)


class LeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields = "__all__"


class LeadFollowUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeadFollowUp
        fields = "__all__"
