from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import PricingRule, Quotation
from .serializers import (
    PricingRuleSerializer,
    QuotationSerializer,
)

from .services import generate_quotation


class PricingRuleViewSet(viewsets.ModelViewSet):
    queryset = PricingRule.objects.all()
    serializer_class = PricingRuleSerializer


class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all().order_by("-id")
    serializer_class = QuotationSerializer

    @action(
        detail=False,
        methods=["get"]
    )
    def generate(self, request):

        lead_id = request.GET.get("lead_id")

        if not lead_id:
            return Response(
                {
                    "error": "lead_id is required"
                },
                status=400
            )

        try:
            result = generate_quotation(
                lead_id
            )

            return Response(result)

        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=400
            )
