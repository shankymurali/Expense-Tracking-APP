from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Expense, Category, ExpenseCollaborator, Reminder, Budget, Card
import datetime

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name')
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name')
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address')
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', )

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'createdon', 'description', 'category', 'paymentMethod', 'address']
        widgets = {
            'createdon': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Date', 'value': datetime.date.today()}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'paymentMethod': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Payment Method', 'default': 'Cash'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
        }

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['deadline', 'name', 'category', 'amount', 'description']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'value': datetime.date.today()}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
        }

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'cardnumber', 'cvc', 'expiry', 'description']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'expiry': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'value': datetime.date.today()}),
        }