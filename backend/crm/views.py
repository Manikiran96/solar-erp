from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Lead, LeadFollowUp
from .serializers import (
    LeadSerializer,
    LeadListSerializer,
    LeadFollowUpSerializer,
)


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all().order_by("-created_at")
    serializer_class = LeadSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = [
        "lead_id",
        "customer_name",
        "mobile",
        "location",
        "state",
        "district",
        "reference_name",
        "assigned_to",
    ]

    ordering_fields = [
        "created_at",
        "updated_at",
        "estimated_cost",
        "expected_capacity",
    ]

    def get_serializer_class(self):
        if self.action == "list":
            return LeadListSerializer
        return LeadSerializer

    def get_queryset(self):
        queryset = Lead.objects.all().order_by("-created_at")

        status = self.request.query_params.get("status")
        source = self.request.query_params.get("lead_source")
        project_type = self.request.query_params.get("project_type")
        category = self.request.query_params.get("customer_category")

        if status:
            queryset = queryset.filter(status=status)

        if source:
            queryset = queryset.filter(lead_source=source)

        if project_type:
            queryset = queryset.filter(project_type=project_type)

        if category:
            queryset = queryset.filter(customer_category=category)

        return queryset

    @action(detail=False, methods=["get"])
    def summary(self, request):
        total_leads = Lead.objects.count()
        new_leads = Lead.objects.filter(status="NEW").count()
        contacted = Lead.objects.filter(status="CONTACTED").count()
        quotation_sent = Lead.objects.filter(status="QUOTATION_SENT").count()
        won = Lead.objects.filter(status="WON").count()
        lost = Lead.objects.filter(status="LOST").count()

        return Response({
            "total_leads": total_leads,
            "new_leads": new_leads,
            "contacted": contacted,
            "quotation_sent": quotation_sent,
            "won": won,
            "lost": lost,
        })


class LeadFollowUpViewSet(viewsets.ModelViewSet):
    queryset = LeadFollowUp.objects.all().order_by("-created_at")
    serializer_class = LeadFollowUpSerializer

    def get_queryset(self):
        queryset = LeadFollowUp.objects.all().order_by("-created_at")
        lead_id = self.request.query_params.get("lead")

        if lead_id:
            queryset = queryset.filter(lead_id=lead_id)

        return queryset
