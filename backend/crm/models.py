from django.db import models


class Lead(models.Model):
    LEAD_STATUS_CHOICES = [
        ("NEW", "New"),
        ("CONTACTED", "Contacted"),
        ("SURVEY_SCHEDULED", "Survey Scheduled"),
        ("QUOTATION_SENT", "Quotation Sent"),
        ("NEGOTIATION", "Negotiation"),
        ("WON", "Won"),
        ("LOST", "Lost"),
    ]

    customer_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    project_type = models.CharField(max_length=100, blank=True, null=True)
    expected_capacity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estimated_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    lead_source = models.CharField(max_length=100, blank=True, null=True)
    reference_name = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=50, choices=LEAD_STATUS_CHOICES, default="NEW")
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
