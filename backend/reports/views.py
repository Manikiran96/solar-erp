from rest_framework.views import APIView
from rest_framework.response import Response

from crm.models import Lead
from customers.models import Customer
from projects.models import Project
from inventory.models import InventoryItem
from finance.models import Invoice, CustomerPayment
from technicians.models import (
    Technician,
    WorkOrder
)


class DashboardView(APIView):

    def get(self, request):

        data = {
            "total_leads": Lead.objects.count(),
            "total_customers": Customer.objects.count(),
            "total_projects": Project.objects.count(),

            "completed_projects":
                Project.objects.filter(
                    project_status="COMPLETED"
                ).count(),

            "pending_projects":
                Project.objects.exclude(
                    project_status="COMPLETED"
                ).count(),

            "inventory_items":
                InventoryItem.objects.count(),

            "invoices":
                Invoice.objects.count(),

            "payments":
                CustomerPayment.objects.count(),

            "technicians":
                Technician.objects.count(),

            "open_work_orders":
                WorkOrder.objects.exclude(
                    status="COMPLETED"
                ).count(),
        }

        return Response(data)
