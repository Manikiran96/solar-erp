from django.db import models

from projects.models import Project


class InventoryItem(models.Model):

    ITEM_TYPES = [
        ("PANEL", "Solar Panel"),
        ("INVERTER", "Inverter"),
        ("BATTERY", "Battery"),
        ("STRUCTURE", "Structure"),
        ("CABLE", "Cable"),
        ("OTHER", "Other"),
    ]

    item_code = models.CharField(
        max_length=50,
        unique=True
    )

    item_name = models.CharField(
        max_length=255
    )

    item_type = models.CharField(
        max_length=50,
        choices=ITEM_TYPES
    )

    unit = models.CharField(
        max_length=50,
        default="NOS"
    )

    stock_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    reorder_level = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        if not self.item_code:

            last_item = (
                InventoryItem.objects
                .order_by("-id")
                .first()
            )

            next_id = (
                last_item.id + 1
                if last_item
                else 1
            )

            self.item_code = (
                f"ITEM{next_id:05d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):

        return (
            f"{self.item_code} - "
            f"{self.item_name}"
        )


class MaterialIssue(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    inventory_item = models.ForeignKey(
        InventoryItem,
        on_delete=models.CASCADE
    )

    quantity_issued = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    issued_to = models.CharField(
        max_length=200
    )

    issued_date = models.DateField()

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return (
            f"{self.project.project_code} - "
            f"{self.inventory_item.item_name}"
        )
