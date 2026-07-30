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
        ("COMMERCIAL", "Commercial"),
        ("INDUSTRIAL", "Industrial"),
        ("AGRICULTURAL", "Agricultural"),
        ("GOVERNMENT", "Government"),
    ]

    LEAD_SOURCE_CHOICES = [
        ("FACEBOOK", "Facebook"),
        ("WEBSITE", "Website"),
        ("REFERENCE", "Reference"),
        ("WALK_IN", "Walk In"),
        ("WHATSAPP", "WhatsApp"),
        ("BROKER", "Broker"),
        ("OTHER", "Other"),
    ]

    lead_id = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True
    )

    customer_name = models.CharField(
        max_length=200
    )

    mobile = models.CharField(
        max_length=20
    )

    alternative_mobile = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    location = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    state = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    district = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    customer_category = models.CharField(
        max_length=50,
        choices=CUSTOMER_CATEGORY_CHOICES
    )

    project_type = models.CharField(
        max_length=50,
        choices=PROJECT_TYPE_CHOICES
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

    sales_person = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    lead_source = models.CharField(
        max_length=50,
        choices=LEAD_SOURCE_CHOICES,
        default="OTHER"
    )

    follow_up_date = models.DateField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=50,
        choices=LEAD_STATUS_CHOICES,
        default="NEW"
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.lead_id:

            last_lead = (
                Lead.objects
                .order_by("-id")
                .first()
            )

            next_id = (
                last_lead.id + 1
                if last_lead
                else 1
            )

            self.lead_id = (
                f"LEAD{next_id:05d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.lead_id} - "
            f"{self.customer_name}"
        )


class LeadFollowUp(models.Model):

    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        related_name="followups"
    )

    followup_date = models.DateField()

    remarks = models.TextField()

    next_followup_date = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.lead.lead_id}"
        )
