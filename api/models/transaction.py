from django.db import models
from .account import Account

class Transaction (models.Model):
    account= models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    TRANSACTION_TYPES = [
        ("DEP","Deposit"),
        ("WDR","Withdrawal"),
        ("TRF","Transfer")
    ]
    type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    description=models.TextField(blank=True)
