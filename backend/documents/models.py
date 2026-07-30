from django.db import models
from customers.models import Customer


class CustomerDocument(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ("AADHAAR", "Aadhaar"),
        ("PAN", "PAN"),
        ("ELECTRICITY_BILL", "Electricity Bill"),
        ("PROPERTY_DOCUMENT", "Property Document"),
        ("SITE_PHOTO", "Site Photo"),
        ("QUOTATION", "Quotation"),
        ("SIGNED_DOCUMENT", "Signed Document"),
        ("SUBSIDY_DOCUMENT", "Subsidy Document"),
        ("INSPECTION_REPORT", "Inspection Report"),
        ("OTHER", "Other"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="documents")
    document_type = models.CharField(max_length=100, choices=DOCUMENT_TYPE_CHOICES)
    document_name = models.CharField(max_length=200)
    file = models.FileField(upload_to="customer_documents/")
    remarks = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.customer_name} - {self.document_type}"
