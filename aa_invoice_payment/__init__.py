"""Alliance Auth invoice payment dashboard addon."""

__all__ = ["default_app_config"]

# Django uses default_app_config to locate app configuration
# when the app is listed in INSTALLED_APPS

default_app_config = "aa_invoice_payment.apps.InvoicePaymentConfig"
