from decimal import Decimal

from crm.models import Lead
from .models import PricingRule


def generate_quotation(lead_id):

    lead = Lead.objects.get(id=lead_id)

    pricing_rule = PricingRule.objects.filter(
        project_type=lead.customer_category,
        installation_mode=lead.project_type,
        min_capacity__lte=lead.expected_capacity,
        max_capacity__gte=lead.expected_capacity,
        active=True
    ).first()

    if not pricing_rule:
        raise Exception(
            "Pricing rule not configured."
        )

    base_amount = (
        lead.expected_capacity *
        pricing_rule.price_per_kw
    )

    gst_amount = (
        base_amount *
        pricing_rule.gst_percent
    ) / Decimal("100")

    final_amount = (
        base_amount +
        gst_amount
    )

    return {
        "lead_id": lead.id,
        "customer_name": lead.customer_name,
        "capacity": lead.expected_capacity,
        "project_type": lead.customer_category,
        "installation_mode": lead.project_type,
        "base_amount": base_amount,
        "gst_amount": gst_amount,
        "final_amount": final_amount,
    }
