from django.contrib import admin
from django.contrib.auth.models import User

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
        "sales_person_user",
        "lead_source",
        "status",
        "is_converted",
        "follow_up_date",
        "created_at",
    ]

    search_fields = [
        "lead_id",
        "customer_name",
        "mobile",
        "sales_person",
        "sales_person_user__username",
    ]

    list_filter = [
        "status",
        "is_converted",
        "lead_source",
        "customer_category",
        "project_type",
    ]

    readonly_fields = [
        "lead_id",
        "is_converted",
    ]

    def formfield_for_foreignkey(
        self,
        db_field,
        request,
        **kwargs
    ):

        if db_field.name == "sales_person_user":

            kwargs["queryset"] = User.objects.filter(
                groups__name="SALES",
                is_active=True
            ).order_by("username")

        return super().formfield_for_foreignkey(
            db_field,
            request,
            **kwargs
        )


@admin.register(LeadFollowUp)
class LeadFollowUpAdmin(admin.ModelAdmin):

    list_display = [
        "lead",
        "followup_date",
        "next_followup_date",
        "created_at",
    ]

    search_fields = [
        "lead__lead_id",
        "lead__customer_name",
        "remarks",
    ]

    list_filter = [
        "followup_date",
        "next_followup_date",
    ]
