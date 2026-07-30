from django.db import models
from projects.models import Project


class ProjectFinance(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="finance")
    project_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    gst = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    subsidy = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    final_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.project.project_id


class Payment(models.Model):
    PAYMENT_MODE_CHOICES = [
        ("UPI", "UPI"),
        ("NEFT", "NEFT"),
        ("RTGS", "RTGS"),
        ("BANK_TRANSFER", "Bank Transfer"),
        ("CHEQUE", "Cheque"),
        ("CASH", "Cash"),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODE_CHOICES)
    utr_number = models.CharField(max_length=100, blank=True, null=True)
    payment_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.project_id} - {self.amount}"
