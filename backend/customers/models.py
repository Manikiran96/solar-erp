from django.db import models


class Customer(models.Model):
    CUSTOMER_CATEGORY_CHOICES = [
        ("RESIDENTIAL", "Residential"),
        ("INDUSTRIAL", "Industrial"),
        ("AGRICULTURAL", "Agricultural"),
        ("COMMERCIAL", "Commercial"),
        ("GOVERNMENT", "Government"),
    ]

    customer_id = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    alternative_mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    pan_number = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CUSTOMER_CATEGORY_CHOICES)
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
