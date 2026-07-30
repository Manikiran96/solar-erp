from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/accounts/", include("accounts.urls")),
    path("api/crm/", include("crm.urls")),
    path("api/quotation/", include("quotation.urls")),
    path("api/customers/", include("customers.urls")),
    path("api/documents/", include("documents.urls")),
    path("api/projects/", include("projects.urls")),
    path("api/inventory/", include("inventory.urls")),
    path("api/technicians/", include("technicians.urls")),
    path("api/finance/", include("finance.urls")),
    path("api/reports/", include("reports.urls")),
]
