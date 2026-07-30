from decimal import Decimal
from .models import PricingRule


def calculate_quotation(project_type, installation_mode, capacity, discount_amount=0):
    capacity = Decimal(str(capacity))
    discount_amount = Decimal(str(discount_amount))

    rule = PricingRule.objects.filter(
        project_type=project_type,
        installation_mode=installation_mode,
        min_capacity__lte=capacity,
        max_capacity__gte=capacity,
        active=True
    ).first()

    if not rule:
        raise ValueError("No pricing rule found for selected project type, installation mode and capacity")

    base_amount = capacity * rule.price_per_kw
    gst_amount = (base_amount * rule.gst_percent) / Decimal("100")
    final_amount = base_amount + gst_amount - discount_amount

    return {
        "base_amount": base_amount,
        "gst_amount": gst_amount,
        "discount_amount": discount_amount,
        "final_amount": final_amount,
        "pricing_rule": rule,
    }
