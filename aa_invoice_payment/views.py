from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Invoice


@login_required
def dashboard(request):
    """Render a dashboard panel showing outstanding invoices."""

    outstanding = Invoice.objects.filter(user=request.user, paid=False)
    context = {
        "outstanding": outstanding,
        "total_due": sum(i.amount for i in outstanding),
    }
    return render(request, "aa_invoice_payment/dashboard.html", context)
