from decimal import Decimal


def calculate_quote(
    capacity,
    price_per_kw,
    gst_percent,
    discount=0,
    subsidy=0
):
    base_amount = Decimal(capacity) * Decimal(price_per_kw)

    gst_amount = (
        base_amount *
        Decimal(gst_percent)
    ) / Decimal("100")

    final_amount = (
        base_amount +
        gst_amount -
        Decimal(discount) -
        Decimal(subsidy)
    )

    return {
        "base_amount": base_amount,
        "gst_amount": gst_amount,
        "final_amount": final_amount
    }
