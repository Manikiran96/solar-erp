from django.urls import path

from .views import (
    SalesDashboardView,
    ProjectDashboardView,
    InventoryDashboardView,
    FinanceDashboardView,
    TechnicianDashboardView,
    ManagementDashboardView,
)

urlpatterns = [

    path(
        "sales-dashboard/",
        SalesDashboardView.as_view()
    ),

    path(
        "project-dashboard/",
        ProjectDashboardView.as_view()
    ),

    path(
        "inventory-dashboard/",
        InventoryDashboardView.as_view()
    ),

    path(
        "finance-dashboard/",
        FinanceDashboardView.as_view()
    ),

    path(
        "technician-dashboard/",
        TechnicianDashboardView.as_view()
    ),

    path(
        "management-dashboard/",
        ManagementDashboardView.as_view()
    ),
]
