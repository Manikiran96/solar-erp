from django.db import models
from projects.models import Project


class Technician(models.Model):
    employee_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProjectAssignment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="technician_assignments")
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, related_name="assignments")
    assigned_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.project_id} - {self.technician.name}"


class ProjectUpdate(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="updates")
    technician = models.ForeignKey(Technician, on_delete=models.SET_NULL, null=True, blank=True)
    update_date = models.DateField(auto_now_add=True)
    structure_installed = models.BooleanField(default=False)
    panels_installed = models.BooleanField(default=False)
    inverter_installed = models.BooleanField(default=False)
    wiring_completed = models.BooleanField(default=False)
    earthing_completed = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.project.project_id} - {self.update_date}"
