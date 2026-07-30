from django.db import models

from customers.models import Customer


class Project(models.Model):

    PROJECT_STATUS = [
        ("NEW", "New"),
        ("SURVEY_DONE", "Survey Done"),
        ("MATERIAL_READY", "Material Ready"),
        ("INSTALLATION_IN_PROGRESS", "Installation In Progress"),
        ("TESTING", "Testing"),
        ("COMPLETED", "Completed"),
    ]

    INSTALLATION_TYPES = [
        ("ON_GRID", "On Grid"),
        ("OFF_GRID", "Off Grid"),
        ("HYBRID", "Hybrid"),
    ]

    project_code = models.CharField(
        max_length=50,
        unique=True
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    project_name = models.CharField(
        max_length=255
    )

    installation_type = models.CharField(
        max_length=50,
        choices=INSTALLATION_TYPES
    )

    capacity_kw = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    project_status = models.CharField(
        max_length=50,
        choices=PROJECT_STATUS,
        default="NEW"
    )

    assigned_technician = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    start_date = models.DateField(
        blank=True,
        null=True
    )

    completion_date = models.DateField(
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

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.project_code:

            last_project = (
                Project.objects
                .order_by("-id")
                .first()
            )

            next_id = (
                last_project.id + 1
                if last_project
                else 1
            )

            self.project_code = (
                f"PROJ{next_id:05d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.project_code} - "
            f"{self.project_name}"
        )
