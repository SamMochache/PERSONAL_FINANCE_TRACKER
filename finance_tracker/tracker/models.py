from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type.capitalize()} - {self.category} (${self.amount})"

from django.db import models
from django.contrib.auth.models import User  # To link transactions to the user

# Category choices
CATEGORY_CHOICES = [
    ('Groceries', 'Groceries'),
    ('Rent', 'Rent'),
    ('Salary', 'Salary'),
    ('Utilities', 'Utilities'),
    ('Entertainment', 'Entertainment'),
    ('Others', 'Others'),
]

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.category} - {self.amount} ({self.date})"

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.category} - {self.amount} ({self.date})"
