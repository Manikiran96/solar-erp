from django.db import models

from projects.models import Project


class Technician(models.Model):

    technician_code = models.CharField(
        max_length=50,
        unique=True
    )

    technician_name = models.CharField(
        max_length=255
    )

    mobile = models.CharField(
        max_length=20
    )

    location = models.CharField(
        max_length=255
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        if not self.technician_code:

            last_tech = (
                Technician.objects
                .order_by("-id")
                .first()
            )

            next_id = (
                last_tech.id + 1
                if last_tech
                else 1
            )

            self.technician_code = (
                f"TECH{next_id:05d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.technician_code} - "
            f"{self.technician_name}"
        )


class WorkOrder(models.Model):

    STATUS_CHOICES = [
        ("ASSIGNED", "Assigned"),
        ("IN_PROGRESS", "In Progress"),
        ("ON_HOLD", "On Hold"),
        ("COMPLETED", "Completed"),
    ]

    work_order_number = models.CharField(
        max_length=50,
        unique=True
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    technician = models.ForeignKey(
        Technician,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="ASSIGNED"
    )

    assigned_date = models.DateField()

    completion_date = models.DateField(
        null=True,
        blank=True
    )

    remarks = models.TextField(
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):

        if not self.work_order_number:

            last_wo = (
                WorkOrder.objects
                .order_by("-id")
                .first()
            )

            next_id = (
                last_wo.id + 1
                if last_wo
                else 1
            )

            self.work_order_number = (
                f"WO{next_id:05d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.work_order_number
