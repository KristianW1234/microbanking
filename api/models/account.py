from django.db import models
from .customer import Customer


class Account(models.Model):
    ACCOUNT_TYPES = [("SAV", "Savings"), ("CHK", "Checking"), ("LOAN", "Loan")]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name="accounts")
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)
    opened_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table="account"