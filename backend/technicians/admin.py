from django.contrib import admin

from .models import (
    Technician,
    WorkOrder
)


@admin.register(Technician)
class TechnicianAdmin(
    admin.ModelAdmin
):

    list_display = [
        "technician_code",
        "technician_name",
        "mobile",
        "location",
        "active",
    ]


@admin.register(WorkOrder)
class WorkOrderAdmin(
    admin.ModelAdmin
):

    list_display = [
        "work_order_number",
        "project",
        "technician",
        "status",
        "assigned_date",
    ]
