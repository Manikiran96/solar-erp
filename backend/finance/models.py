from django.db import models

from customers.models import Customer
from projects.models import Project


class CustomerPayment(models.Model):

    PAYMENT_MODES = [
        ("CASH", "Cash"),
        ("UPI", "UPI"),
        ("BANK_TRANSFER", "Bank Transfer"),
        ("CHEQUE", "Cheque"),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    invoice_number = models.CharField(
        max_length=100
    )

    payment_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    payment_mode = models.CharField(
        max_length=50,
        choices=PAYMENT_MODES
    )

    payment_date = models.DateField()

    transaction_reference = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.invoice_number}"
        )


class Invoice(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PARTIAL", "Partial"),
        ("PAID", "Paid"),
    ]

    invoice_number = models.CharField(
        max_length=100,
        unique=True
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    amount_received = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    balance_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    invoice_status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    invoice_date = models.DateField()

    due_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        self.balance_amount = (
            self.total_amount -
            self.amount_received
        )

        if self.balance_amount <= 0:
            self.invoice_status = "PAID"
        elif self.amount_received > 0:
            self.invoice_status = "PARTIAL"
        else:
            self.invoice_status = "PENDING"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number
