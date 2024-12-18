from django.db import models
from django.contrib.auth.models import User
from .utils import convert_currency

# Category choices
EXPENSE_CATEGORIES = [
    ('Groceries', 'Groceries'),
    ('Rent', 'Rent'),
    ('Utilities', 'Utilities'),
    ('Entertainment', 'Entertainment'),
    ('Others', 'Others'),
]

INCOME_CATEGORIES = [
    ('Salary', 'Salary'),
    ('Bonus', 'Bonus'),
    ('Investments', 'Investments'),
    ('Others', 'Others'),
]

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=EXPENSE_CATEGORIES)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount} ({self.date})"

    def convert_amount(self, to_currency):
        """
        Converts the expense amount to the given currency using a currency conversion API.
        """
        return convert_currency(self.amount, 'USD', to_currency)  # Convert from USD to user's preferred currency


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=INCOME_CATEGORIES)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount} ({self.date})"

    def convert_amount(self, to_currency):
        """
        Converts the income amount to the given currency using a currency conversion API.
        """
        return convert_currency(self.amount, 'USD', to_currency)
    
    # models.py

CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('EUR', 'Euro'),
    ('GBP', 'British Pound'),
    ('KES', 'Kenyan Shilling'),
    ('INR', 'Indian Rupee'),
    # Add more currencies as needed
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')

    def __str__(self):
        return f"{self.user.username}'s Profile"
