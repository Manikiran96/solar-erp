from django.db import models
from crm.models import Lead


class Customer(models.Model):

    CUSTOMER_CATEGORY_CHOICES = [
        ("RESIDENTIAL", "Residential"),
        ("COMMERCIAL", "Commercial"),
        ("INDUSTRIAL", "Industrial"),
        ("AGRICULTURAL", "Agricultural"),
        ("GOVERNMENT", "Government"),
    ]

    customer_code = models.CharField(
        max_length=50,
        unique=True
    )

    lead = models.ForeignKey(
        Lead,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
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

    aadhaar_number = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    pan_number = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    customer_category = models.CharField(
        max_length=50,
        choices=CUSTOMER_CATEGORY_CHOICES
    )

    address = models.TextField(
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

    pincode = models.CharField(
        max_length=20,
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

        if not self.customer_code:

            last_customer = (
                Customer.objects
                .order_by("-id")
                .first()
            )

            next_id = (
                last_customer.id + 1
                if last_customer
                else 1
            )

            self.customer_code = (
                f"CUST{next_id:05d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.customer_code}"
            f" - "
            f"{self.customer_name}"
        )
