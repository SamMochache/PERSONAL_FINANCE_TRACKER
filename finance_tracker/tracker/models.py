from django.db import models
from django.contrib.auth.models import User
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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
        Converts the amount to the given currency using a currency conversion API.
        """
        base_currency = 'USD'
        api_key = os.getenv('EXCHANGE_RATE_API_KEY')  # Fetch API key from .env
        endpoint = f"https://open.er-api.com/v6/latest/{base_currency}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            rates = response.json().get("rates", {})
            conversion_rate = rates.get(to_currency)
            if conversion_rate:
                return round(self.amount * conversion_rate, 2)
        return self.amount  # Return the original amount if conversion fails


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
        Converts the amount to the given currency using a currency conversion API.
        """
        base_currency = 'USD'
        api_key = os.getenv('EXCHANGE_RATE_API_KEY')  # Fetch API key from .env
        endpoint = f"https://open.er-api.com/v6/latest/{base_currency}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            rates = response.json().get("rates", {})
            conversion_rate = rates.get(to_currency)
            if conversion_rate:
                return round(self.amount * conversion_rate, 2)
        return self.amount
