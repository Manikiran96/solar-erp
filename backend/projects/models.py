from django.db import models
from customers.models import Customer


class Project(models.Model):
    PROJECT_STATUS_CHOICES = [
        ("CREATED", "Created"),
        ("MATERIAL_ASSIGNED", "Material Assigned"),
        ("INSTALLATION_STARTED", "Installation Started"),
        ("STRUCTURE_INSTALLED", "Structure Installed"),
        ("PANELS_INSTALLED", "Panels Installed"),
        ("INVERTER_INSTALLED", "Inverter Installed"),
        ("WIRING_COMPLETED", "Wiring Completed"),
        ("TESTING_COMPLETED", "Testing Completed"),
        ("COMMISSIONED", "Commissioned"),
        ("COMPLETED", "Completed"),
    ]

    PROJECT_TYPE_CHOICES = [
        ("ON_GRID", "On Grid"),
        ("OFF_GRID", "Off Grid"),
        ("HYBRID", "Hybrid"),
    ]

    project_id = models.CharField(max_length=50, unique=True)
    project_name = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="projects")
    capacity = models.DecimalField(max_digits=10, decimal_places=2)
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPE_CHOICES)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, choices=PROJECT_STATUS_CHOICES, default="CREATED")
    start_date = models.DateField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_id
