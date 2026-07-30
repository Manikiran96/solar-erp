from django.contrib import admin

from .models import (
    CustomerPayment,
    Invoice
)


@admin.register(CustomerPayment)
class CustomerPaymentAdmin(
    admin.ModelAdmin
):

    list_display = [
        "invoice_number",
        "customer",
        "payment_amount",
        "payment_mode",
        "payment_date",
    ]


@admin.register(Invoice)
class InvoiceAdmin(
    admin.ModelAdmin
):

    list_display = [
        "invoice_number",
        "customer",
        "total_amount",
        "amount_received",
        "balance_amount",
        "invoice_status",
    ]
