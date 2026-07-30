from django.db import models
from projects.models import Project


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=200)
    broker_name = models.CharField(max_length=200, blank=True, null=True)
    gst_number = models.CharField(max_length=50, blank=True, null=True)
    contact_person = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.supplier_name


class StockReceipt(models.Model):
    grn_number = models.CharField(max_length=100, unique=True)
    invoice_number = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=50, blank=True, null=True)
    received_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="receipts")
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.grn_number


class StockItem(models.Model):
    receipt = models.ForeignKey(StockReceipt, on_delete=models.CASCADE, related_name="stock_items")
    serial_number = models.CharField(max_length=100, unique=True)
    material_name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)
    rating = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    available_quantity = models.IntegerField(default=1)
    assigned_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.serial_number


class MaterialAllocation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="material_allocations")
    stock_item = models.ForeignKey(StockItem, on_delete=models.CASCADE, related_name="allocations")
    quantity = models.IntegerField()
    assigned_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.project_id} - {self.stock_item.material_name}"
