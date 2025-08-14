from django.urls import path

from . import views


app_name = "aa_invoice_payment"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
]
