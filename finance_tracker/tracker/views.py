from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Transaction, models

@login_required
def dashboard(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user).order_by('-date')[:5]  # Last 5 transactions
    total_income = Transaction.objects.filter(user=user, transaction_type='income').aggregate(total=models.Sum('amount'))['total'] or 0
    total_expense = Transaction.objects.filter(user=user, transaction_type='expense').aggregate(total=models.Sum('amount'))['total'] or 0
    balance = total_income - total_expense

    context = {
        'user': user,
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }
    return render(request, 'tracker/dashboard.html', context)

