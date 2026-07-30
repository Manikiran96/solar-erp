from django.contrib import admin
from django.urls import path, include

from .views import (
    login_view,
    logout_view,
    role_dashboard,
    admin_dashboard_page,
    sales_dashboard_page,
    finance_dashboard_page,
    technician_dashboard_page,
    management_dashboard_page,
)


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "login/",
        login_view,
        name="login"
    ),

    path(
        "logout/",
        logout_view,
        name="logout"
    ),

    path(
        "dashboard/",
        role_dashboard,
        name="role_dashboard"
    ),

    path(
        "dashboard/admin/",
        admin_dashboard_page,
        name="admin_dashboard"
    ),

    path(
        "dashboard/sales/",
        sales_dashboard_page,
        name="sales_dashboard_page"
    ),

    path(
        "dashboard/finance/",
        finance_dashboard_page,
        name="finance_dashboard_page"
    ),

    path(
        "dashboard/technician/",
        technician_dashboard_page,
        name="technician_dashboard_page"
    ),

    path(
        "dashboard/management/",
        management_dashboard_page,
        name="management_dashboard_page"
    ),

    path(
        "api/accounts/",
        include("accounts.urls")
    ),

    path(
        "api/crm/",
        include("crm.urls")
    ),

    path(
        "api/quotation/",
        include("quotation.urls")
    ),

    path(
        "api/customers/",
        include("customers.urls")
    ),

    path(
        "api/documents/",
        include("documents.urls")
    ),

    path(
        "api/projects/",
        include("projects.urls")
    ),

    path(
        "api/inventory/",
        include("inventory.urls")
    ),

    path(
        "api/technicians/",
        include("technicians.urls")
    ),

    path(
        "api/finance/",
        include("finance.urls")
    ),

    path(
        "api/reports/",
        include("reports.urls")
    ),
]
