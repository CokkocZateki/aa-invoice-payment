# aa-invoice-payment

Addon for Alliance Auth that displays outstanding invoices on the dashboard.

## Installation

1. Add `aa_invoice_payment` to `INSTALLED_APPS`.
2. Include the URLs in your project:

   ```python
   path("invoices/", include("aa_invoice_payment.urls")),
   ```
3. Run migrations to create the `Invoice` model.

## Usage

Navigate to `/invoices/dashboard/` to view outstanding payments for the
current user. Integrate the rendered template into a dashboard panel or MOTD.
