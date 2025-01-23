from django.db import models
from accounts.models import StudentProfile
from books.models import BooksDetails

from .constants import TRANSACTION_TYPE
# Create your models here.

class Transaction(models.Model):
    profile = models.ForeignKey(StudentProfile, related_name= 'transactions', on_delete=models.CASCADE)
    book = models.ForeignKey(BooksDetails, on_delete=models.CASCADE, default=1)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    balance_after_transactions = models.DecimalField(decimal_places=2, max_digits=12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']