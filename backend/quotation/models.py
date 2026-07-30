from django.db import models
from crm.models import Lead


class PricingRule(models.Model):
    project_type = models.CharField(max_length=100)
    installation_mode = models.CharField(max_length=100)
    min_capacity = models.DecimalField(max_digits=10, decimal_places=2)
    max_capacity = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_kw = models.DecimalField(max_digits=12, decimal_places=2)
    gst_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.project_type} - {self.installation_mode}"


class Quotation(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="quotations")
    capacity = models.DecimalField(max_digits=10, decimal_places=2)
    project_type = models.CharField(max_length=100)
    installation_mode = models.CharField(max_length=100)
    base_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    gst_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    final_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quotation for {self.lead.customer_name}"
