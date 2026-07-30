from django.contrib import admin
from .models import Lead, LeadFollowUp


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = [
        "lead_id",
        "customer_name",
        "mobile",
        "customer_category",
        "project_type",
        "expected_capacity",
        "estimated_cost",
        "lead_source",
        "status",
        "assigned_to",
        "created_at",
    ]

    search_fields = [
        "lead_id",
        "customer_name",
        "mobile",
        "location",
        "reference_name",
    ]

    list_filter = [
        "status",
        "lead_source",
        "project_type",
        "customer_category",
        "created_at",
    ]


@admin.register(LeadFollowUp)
class LeadFollowUpAdmin(admin.ModelAdmin):
    list_display = [
        "lead",
        "followup_date",
        "followup_time",
        "status",
        "created_at",
    ]

    search_fields = [
        "lead__lead_id",
        "lead__customer_name",
        "notes",
    ]

    list_filter = [
        "status",
        "followup_date",
    ]
