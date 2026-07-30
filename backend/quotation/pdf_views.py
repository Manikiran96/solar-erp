import io

from django.contrib.auth.decorators import login_required
from django.http import (
    FileResponse,
    HttpResponse,
    HttpResponseForbidden
)

from reportlab.pdfgen import canvas

from .models import Quotation


@login_required
def quotation_pdf(request, pk):

    if not (
        request.user.is_superuser
        or
        request.user.groups.filter(
            name__in=[
                "ADMIN",
                "SALES",
                "MANAGEMENT"
            ]
        ).exists()
    ):

        return HttpResponseForbidden(
            "Access Denied"
        )

    try:

        quotation = Quotation.objects.get(
            id=pk
        )

    except Quotation.DoesNotExist:

        return HttpResponse(
            "Quotation not found",
            status=404
        )

    buffer = io.BytesIO()

    pdf = canvas.Canvas(buffer)

    # Header

    pdf.setFont(
        "Helvetica-Bold",
        18
    )

    pdf.drawString(
        180,
        800,
        "SOLAR QUOTATION"
    )

    pdf.setFont(
        "Helvetica",
        12
    )

    # Quotation Details

    pdf.drawString(
        50,
        750,
        f"Quotation Number: {quotation.quotation_number}"
    )

    pdf.drawString(
        50,
        730,
        f"Customer Name: {quotation.lead.customer_name}"
    )

    pdf.drawString(
        50,
        710,
        f"Mobile: {quotation.lead.mobile}"
    )

    if quotation.lead.email:

        pdf.drawString(
            50,
            690,
            f"Email: {quotation.lead.email}"
        )

    # Project Details

    pdf.drawString(
        50,
        650,
        f"Project Type: {quotation.project_type}"
    )

    pdf.drawString(
        50,
        630,
        f"Installation Mode: {quotation.installation_mode}"
    )

    pdf.drawString(
        50,
        610,
        f"Capacity: {quotation.capacity_kw} KW"
    )

    # Pricing

    pdf.drawString(
        50,
        560,
        f"Base Amount: Rs. {quotation.base_amount}"
    )

    pdf.drawString(
        50,
        540,
        f"GST Amount: Rs. {quotation.gst_amount}"
    )

    pdf.drawString(
        50,
        520,
        f"Discount Amount: Rs. {quotation.discount_amount}"
    )

    pdf.drawString(
        50,
        500,
        f"Subsidy Amount: Rs. {quotation.subsidy_amount}"
    )

    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        50,
        460,
        f"Final Amount: Rs. {quotation.final_amount}"
    )

    # Remarks

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(
        50,
        420,
        "Remarks:"
    )

    remarks = quotation.remarks or "NA"

    pdf.drawString(
        120,
        420,
        remarks[:80]
    )

    # Footer

    pdf.drawString(
        50,
        200,
        "Thank you for choosing our Solar Solutions."
    )

    pdf.drawString(
        50,
        180,
        "This is a system generated quotation."
    )

    pdf.showPage()

    pdf.save()

    buffer.seek(0)

    return FileResponse(
        buffer,
        as_attachment=True,
        filename=f"{quotation.quotation_number}.pdf"
    )
