from rest_framework import serializers
from django.contrib.auth.models import User

from .models import (
    Lead,
    LeadFollowUp
)


class SalesUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        ]


class LeadSerializer(serializers.ModelSerializer):

    sales_person_username = serializers.CharField(
        source="sales_person_user.username",
        read_only=True
    )

    class Meta:

        model = Lead

        fields = "__all__"

        read_only_fields = [
            "lead_id",
            "is_converted",
            "sales_person_username",
        ]

    def validate(self, data):

        instance = self.instance

        if (
            instance
            and
            instance.is_converted
        ):

            raise serializers.ValidationError(
                "Converted leads cannot be modified."
            )

        return data


class LeadFollowUpSerializer(serializers.ModelSerializer):

    class Meta:

        model = LeadFollowUp

        fields = "__all__"
