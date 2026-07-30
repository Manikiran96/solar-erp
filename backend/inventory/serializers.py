from rest_framework import serializers

from .models import (
    InventoryItem,
    MaterialIssue
)


class InventoryItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryItem
        fields = "__all__"


class MaterialIssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialIssue
        fields = "__all__"
