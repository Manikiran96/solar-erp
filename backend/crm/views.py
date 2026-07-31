from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    Lead,
    LeadFollowUp
)

from .serializers import (
    LeadSerializer,
    LeadFollowUpSerializer,
    SalesUserSerializer
)

from core.permissions import (
    IsAdmin,
    IsSales
)


class LeadViewSet(viewsets.ModelViewSet):

    serializer_class = LeadSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        return (
            Lead.objects
            .filter(
                is_converted=False
            )
            .exclude(
                status="LOST"
            )
            .order_by("-id")
        )

    @action(
        detail=False,
        methods=["get"],
        url_path="sales-users"
    )
    def sales_users(self, request):

        users = User.objects.filter(
            groups__name="SALES",
            is_active=True
        ).order_by("username")

        serializer = SalesUserSerializer(
            users,
            many=True
        )

        return Response(
            serializer.data
        )


class ConvertedLeadViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = LeadSerializer

    permission_classes = [
        IsAuthenticated
    ]

    queryset = (
        Lead.objects
        .filter(
            is_converted=True
        )
        .order_by("-id")
    )


class LostLeadViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = LeadSerializer

    permission_classes = [
        IsAuthenticated
    ]

    queryset = (
        Lead.objects
        .filter(
            status="LOST"
        )
        .order_by("-id")
    )


class LeadFollowUpViewSet(viewsets.ModelViewSet):

    queryset = (
        LeadFollowUp.objects
        .all()
        .order_by("-id")
    )

    serializer_class = LeadFollowUpSerializer

    permission_classes = [
        IsAuthenticated
    ]
