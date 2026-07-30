from decimal import Decimal
from .models import Payment


def get_project_payment_summary(project):
    total_received = Payment.objects.filter(project=project).values_list("amount", flat=True)
    total_received = sum(total_received, Decimal("0"))

    final_amount = Decimal("0")
    if hasattr(project, "finance"):
        final_amount = project.finance.final_amount

    balance_amount = final_amount - total_received

    if total_received == 0:
        payment_status = "PENDING"
    elif balance_amount <= 0:
        payment_status = "PAID"
    else:
        payment_status = "PARTIALLY_PAID"

    return {
        "final_amount": final_amount,
        "total_received": total_received,
        "balance_amount": balance_amount,
        "payment_status": payment_status,
    }
