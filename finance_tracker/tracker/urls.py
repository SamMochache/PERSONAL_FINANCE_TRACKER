from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-income/', views.add_income, name='add_income'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('income/add/', views.add_income, name='income_form'),
    path('expense/add/', views.add_expense, name='expense_form'),
    path('google-menu/', views.google_menu, name='google_menu'),
]
