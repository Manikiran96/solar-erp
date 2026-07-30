from django.db import models
from customers.models import Customer


class CustomerDocument(models.Model):

    DOCUMENT_TYPES = [
        ("AADHAAR", "Aadhaar"),
        ("PAN", "PAN"),
        ("ELECTRICITY_BILL", "Electricity Bill"),
        ("SITE_SURVEY", "Site Survey"),
        ("PROPERTY_DOC", "Property Document"),
        ("QUOTATION", "Quotation"),
        ("AGREEMENT", "Agreement"),
        ("OTHER", "Other"),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    document_type = models.CharField(
        max_length=50,
        choices=DOCUMENT_TYPES
    )

    document_name = models.CharField(
        max_length=255
    )

    file_path = models.CharField(
        max_length=500
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.customer.customer_code}"
            f" - "
            f"{self.document_type}"
        )
