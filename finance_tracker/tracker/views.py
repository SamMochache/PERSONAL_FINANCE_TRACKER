from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Expense, Income
from .forms import IncomeForm, ExpenseForm


@login_required(login_url='/accounts/google/login/')
def dashboard(request):
    user = request.user

    # Retrieve recent transactions
    recent_expenses = Expense.objects.filter(user=user).order_by('-date')[:5]  # Last 5 expenses
    recent_income = Income.objects.filter(user=user).order_by('-date')[:5]    # Last 5 income records

    # Calculate totals
    total_income = Income.objects.filter(user=user).aggregate(total=Sum('amount'))['total'] or 0
    total_expense = Expense.objects.filter(user=user).aggregate(total=Sum('amount'))['total'] or 0
    balance = total_income - total_expense

    # Context for rendering
    context = {
        'user': user,
        'recent_expenses': recent_expenses,
        'recent_income': recent_income,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }
    return render(request, 'tracker/dashboard.html', context)
@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user  # Associate with the logged-in user
            income.save()
            return redirect('dashboard')  # Redirect to dashboard after saving
    else:
        form = IncomeForm()
    return render(request, 'tracker/add_income.html', {'form': form})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Associate with the logged-in user
            expense.save()
            return redirect('dashboard')  # Redirect to dashboard after saving
    else:
        form = ExpenseForm()
    return render(request, 'tracker/add_expense.html', {'form': form})

def home(request):
    """Render the homepage."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'base.html')