from django.contrib import admin

from .models import (
    Lead,
    LeadFollowUp
)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):

    list_display = [
        "lead_id",
        "customer_name",
        "mobile",
        "sales_person",
        "lead_source",
        "status",
        "follow_up_date",
    ]

    search_fields = [
        "lead_id",
        "customer_name",
        "mobile",
        "sales_person",
    ]


@admin.register(LeadFollowUp)
class LeadFollowUpAdmin(admin.ModelAdmin):

    list_display = [
        "lead",
        "followup_date",
        "next_followup_date",
    ]
