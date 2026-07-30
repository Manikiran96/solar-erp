from django.contrib import admin

from .models import (
    InventoryItem,
    MaterialIssue
)


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):

    list_display = [
        "item_code",
        "item_name",
        "item_type",
        "stock_quantity",
        "reorder_level",
    ]

    search_fields = [
        "item_code",
        "item_name",
    ]


@admin.register(MaterialIssue)
class MaterialIssueAdmin(admin.ModelAdmin):

    list_display = [
        "project",
        "inventory_item",
        "quantity_issued",
        "issued_to",
        "issued_date",
    ]
