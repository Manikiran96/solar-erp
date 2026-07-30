from django.db import models
from crm.models import Lead


class PricingRule(models.Model):

    PROJECT_TYPES = [
        ("RESIDENTIAL", "Residential"),
        ("COMMERCIAL", "Commercial"),
        ("GOVERNMENT", "Government"),
        ("INDUSTRIAL", "Industrial"),
        ("AGRICULTURAL", "Agricultural"),
    ]

    INSTALLATION_TYPES = [
        ("ON_GRID", "On Grid"),
        ("OFF_GRID", "Off Grid"),
        ("HYBRID", "Hybrid"),
    ]

    project_type = models.CharField(
        max_length=50,
        choices=PROJECT_TYPES
    )

    installation_mode = models.CharField(
        max_length=50,
        choices=INSTALLATION_TYPES
    )

    min_capacity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    max_capacity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    price_per_kw = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    gst_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=18
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.project_type} - "
            f"{self.installation_mode}"
        )


class Quotation(models.Model):

    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        related_name="quotations"
    )

    quotation_number = models.CharField(
        max_length=50,
        unique=True
    )

    project_type = models.CharField(
        max_length=50
    )

    installation_mode = models.CharField(
        max_length=50
    )

    capacity_kw = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    base_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    gst_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    discount_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    subsidy_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    final_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.quotation_number
