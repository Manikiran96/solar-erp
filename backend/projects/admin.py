from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(
    admin.ModelAdmin
):

    list_display = [
        "project_code",
        "project_name",
        "customer",
        "capacity_kw",
        "project_status",
        "assigned_technician",
    ]

    search_fields = [
        "project_code",
        "project_name",
    ]

    list_filter = [
        "project_status",
        "installation_type",
    ]
