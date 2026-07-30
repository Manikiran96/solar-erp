from rest_framework.views import APIView
from rest_framework.response import Response

from crm.models import Lead
from customers.models import Customer
from projects.models import Project
from inventory.models import InventoryItem, MaterialIssue
from finance.models import Invoice, CustomerPayment
from technicians.models import Technician, WorkOrder


class SalesDashboardView(APIView):

    def get(self, request):

        return Response({

            "total_leads":
                Lead.objects.count(),

            "new_leads":
                Lead.objects.filter(
                    status="NEW"
                ).count(),

            "won_leads":
                Lead.objects.filter(
                    status="WON"
                ).count(),

            "lost_leads":
                Lead.objects.filter(
                    status="LOST"
                ).count(),

            "facebook_leads":
                Lead.objects.filter(
                    lead_source="FACEBOOK"
                ).count(),

            "website_leads":
                Lead.objects.filter(
                    lead_source="WEBSITE"
                ).count(),

            "reference_leads":
                Lead.objects.filter(
                    lead_source="REFERENCE"
                ).count(),

            "whatsapp_leads":
                Lead.objects.filter(
                    lead_source="WHATSAPP"
                ).count(),
        })


class ProjectDashboardView(APIView):

    def get(self, request):

        return Response({

            "total_projects":
                Project.objects.count(),

            "completed_projects":
                Project.objects.filter(
                    project_status="COMPLETED"
                ).count(),

            "pending_projects":
                Project.objects.exclude(
                    project_status="COMPLETED"
                ).count(),

            "survey_done":
                Project.objects.filter(
                    project_status="SURVEY_DONE"
                ).count(),

            "installation_in_progress":
                Project.objects.filter(
                    project_status="INSTALLATION_IN_PROGRESS"
                ).count(),
        })


class InventoryDashboardView(APIView):

    def get(self, request):

        return Response({

            "inventory_items":
                InventoryItem.objects.count(),

            "material_issues":
                MaterialIssue.objects.count(),
        })


class FinanceDashboardView(APIView):

    def get(self, request):

        return Response({

            "total_invoices":
                Invoice.objects.count(),

            "payments_received":
                CustomerPayment.objects.count(),

            "paid_invoices":
                Invoice.objects.filter(
                    invoice_status="PAID"
                ).count(),

            "pending_invoices":
                Invoice.objects.filter(
                    invoice_status="PENDING"
                ).count(),
        })


class TechnicianDashboardView(APIView):

    def get(self, request):

        return Response({

            "technicians":
                Technician.objects.count(),

            "open_work_orders":
                WorkOrder.objects.exclude(
                    status="COMPLETED"
                ).count(),

            "completed_work_orders":
                WorkOrder.objects.filter(
                    status="COMPLETED"
                ).count(),
        })


class ManagementDashboardView(APIView):

    def get(self, request):

        return Response({

            "leads":
                Lead.objects.count(),

            "customers":
                Customer.objects.count(),

            "projects":
                Project.objects.count(),

            "inventory_items":
                InventoryItem.objects.count(),

            "payments":
                CustomerPayment.objects.count(),

            "technicians":
                Technician.objects.count(),

            "work_orders":
                WorkOrder.objects.count(),
        })
