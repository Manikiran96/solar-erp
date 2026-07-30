from rest_framework import serializers
from .models import PricingRule, Quotation


class PricingRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingRule
        fields = "__all__"


class QuotationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quotation
        fields = "__all__"
