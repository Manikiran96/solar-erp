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

    PROJECT_TYPE_CHOICES = [
        ("ON_GRID", "On Grid"),
        ("OFF_GRID", "Off Grid"),
        ("HYBRID", "Hybrid"),
    ]

    CUSTOMER_CATEGORY_CHOICES = [
        ("RESIDENTIAL", "Residential"),
        ("INDUSTRIAL", "Industrial"),
        ("AGRICULTURAL", "Agricultural"),
        ("COMMERCIAL", "Commercial"),
        ("GOVERNMENT", "Government"),
    ]

    LEAD_SOURCE_CHOICES = [
        ("FACEBOOK", "Facebook"),
        ("WEBSITE", "Website"),
        ("REFERENCE", "Reference"),
        ("WALK_IN", "Walk In"),
        ("BROKER", "Broker"),
        ("EXISTING_CUSTOMER", "Existing Customer"),
        ("MARKETING_CAMPAIGN", "Marketing Campaign"),
        ("OTHER", "Other"),
    ]

    lead_id = models.CharField(max_length=50, unique=True, blank=True, null=True)

    customer_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    alternative_mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    location = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)

    customer_category = models.CharField(
        max_length=50,
        choices=CUSTOMER_CATEGORY_CHOICES,
        default="RESIDENTIAL"
    )

    project_type = models.CharField(
        max_length=50,
        choices=PROJECT_TYPE_CHOICES,
        default="ON_GRID"
    )

    expected_capacity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    estimated_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    lead_source = models.CharField(
        max_length=50,
        choices=LEAD_SOURCE_CHOICES,
        default="OTHER"
    )

    reference_name = models.CharField(max_length=200, blank=True, null=True)
    reference_mobile = models.CharField(max_length=20, blank=True, null=True)

    status = models.CharField(
        max_length=50,
        choices=LEAD_STATUS_CHOICES,
        default="NEW"
    )

    remarks = models.TextField(blank=True, null=True)

    created_by = models.CharField(max_length=100, blank=True, null=True)
    assigned_to = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.lead_id:
            last_lead = Lead.objects.order_by("-id").first()
            if last_lead:
                next_id = last_lead.id + 1
            else:
                next_id = 1
            self.lead_id = f"LEAD{next_id:05d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.lead_id} - {self.customer_name}"


class LeadFollowUp(models.Model):
    FOLLOW_UP_STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        related_name="followups"
    )

    followup_date = models.DateField()
    followup_time = models.TimeField(blank=True, null=True)

    notes = models.TextField()
    next_action = models.CharField(max_length=255, blank=True, null=True)

    status = models.CharField(
        max_length=50,
        choices=FOLLOW_UP_STATUS_CHOICES,
        default="OPEN"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lead.lead_id} - {self.followup_date}"
