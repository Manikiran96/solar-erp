from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from crm.models import Lead

from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(
    viewsets.ModelViewSet
):

    queryset = (
        Customer.objects
        .all()
        .order_by("-id")
    )

    serializer_class = (
        CustomerSerializer
    )

    @action(
        detail=False,
        methods=["post"]
    )
    def convert_lead(
        self,
        request
    ):

        lead_id = request.data.get(
            "lead_id"
        )

        lead = Lead.objects.get(
            id=lead_id
        )

        customer = Customer.objects.create(
            lead=lead,
            customer_name=lead.customer_name,
            mobile=lead.mobile,
            alternative_mobile=(
                lead.alternative_mobile
            ),
            email=lead.email,
            customer_category=(
                lead.customer_category
            ),
            state=lead.state,
            district=lead.district
        )

        return Response({
            "message":
                "Customer created successfully",
            "customer_id":
                customer.id,
            "customer_code":
                customer.customer_code
        })
