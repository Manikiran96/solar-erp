from django.contrib import admin

from .models import CustomerDocument


@admin.register(CustomerDocument)
class CustomerDocumentAdmin(
    admin.ModelAdmin
):

    list_display = [
        "customer",
        "document_type",
        "document_name",
        "uploaded_at",
    ]

    search_fields = [
        "document_name",
    ]
