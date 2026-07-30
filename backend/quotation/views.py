from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    PricingRule,
    Quotation
)

from .serializers import (
    PricingRuleSerializer,
    QuotationSerializer
)

from .services import calculate_quote


class PricingRuleViewSet(viewsets.ModelViewSet):

    queryset = PricingRule.objects.all()

    serializer_class = PricingRuleSerializer


class QuotationViewSet(viewsets.ModelViewSet):

    queryset = Quotation.objects.all()

    serializer_class = QuotationSerializer

    @action(
        detail=False,
        methods=["post"]
    )
    def calculate(self, request):

        result = calculate_quote(
            request.data["capacity"],
            request.data["price_per_kw"],
            request.data["gst_percent"],
            request.data.get("discount", 0),
            request.data.get("subsidy", 0)
        )

        return Response(result)
