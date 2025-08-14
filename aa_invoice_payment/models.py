from django.conf import settings
from django.db import models


class Invoice(models.Model):
    """Represents an outstanding payment for a user."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    issued = models.DateField()
    due = models.DateField()
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ["due"]

    def __str__(self):
        status = "paid" if self.paid else "due"
        return f"Invoice {self.pk} for {self.user} ({status})"
