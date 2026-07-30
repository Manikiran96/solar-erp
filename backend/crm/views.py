from rest_framework import viewsets

from .models import (
    Lead,
    LeadFollowUp
)

from .serializers import (
    LeadSerializer,
    LeadFollowUpSerializer
)
from rest_framework.permissions import IsAuthenticated

from core.permissions import (
    IsAdmin,
    IsSales
)

class LeadViewSet(viewsets.ModelViewSet):
 
    queryset = (
        Lead.objects
        .all()
        .order_by("-id")
    )
    permission_classes = [IsAuthenticated]
    serializer_class = LeadSerializer


class LeadFollowUpViewSet(viewsets.ModelViewSet):

    queryset = (
        LeadFollowUp.objects
        .all()
        .order_by("-id")
    )

    serializer_class = LeadFollowUpSerializer
