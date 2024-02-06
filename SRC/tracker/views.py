from django.shortcuts import render

from django.shortcuts import render, redirect
from django.db.models import Count, Sum
from django.contrib.auth import authenticate, login, logout
from .models import Expense, Category, Reminder
from .forms import SignupForm, LoginForm, ExpenseForm, CategoryForm, ReminderForm

import datetime


# Home page
def index(request):
    if not request.user.is_authenticated:
        return redirect("login")

    expenses_by_date = {}
    if request.method == "POST":
        searchbox_main = request.POST.get("searchbox-main")
        if searchbox_main:
            for expense in Expense.objects.filter(owner=request.user).filter(
                description__icontains=searchbox_main
            ).order_by("-date") | Expense.objects.filter(owner=request.user).filter(
                category__name__icontains=searchbox_main
            ).order_by(
                "-date"
            ):
                if expense.date not in expenses_by_date:
                    expenses_by_date[expense.date] = [expense]
                else:
                    expenses_by_date[expense.date].append(expense)
    else:
        for expense in Expense.objects.filter(owner=request.user).order_by("-date"):
            if expense.date not in expenses_by_date:
                expenses_by_date[expense.date] = [expense]
            else:
                expenses_by_date[expense.date].append(expense)

    return render(
        request,
        "index.html",
        {
            "expenseform": ExpenseForm(),
            "expenses": expenses_by_date,
            "categories": Category.objects.annotate(
                count=Count("expense"),
                total_amount=Sum("expense__amount"),
            ),
        },
    )


# signup page
def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "register.html", {"form": form})


# login page
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


# logout page
def user_logout(request):
    logout(request)
    return redirect("login")


# create expense page
def create_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.owner = request.user
            expense.save()
            return redirect("home")
    return redirect("home")


# delete expense
def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    return redirect("home")


# manage category page
def manage_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_category")
    return render(
        request,
        "manage_category.html",
        {
            "addcategory": CategoryForm(),
            "categories": Category.objects.annotate(
                count=Count("expense"),
                total_amount=Sum("expense__amount"),
            ),
        },
    )


# delete category
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect("manage_category")


# reminder page
def reminder(request):
    if request.method == "POST":
        form = ReminderForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            return redirect("reminders")

    reminder_by_date = {}
    overdue_reminders = {}
    done_reminders = {}
    for reminder in Reminder.objects.filter(
        owner=request.user, done=False, deadline__gte=datetime.date.today()
    ).order_by("-deadline"):
        if reminder.deadline not in reminder_by_date:
            reminder_by_date[reminder.deadline] = [reminder]
        else:
            reminder_by_date[reminder.deadline].append(reminder)

    for reminder in Reminder.objects.filter(
        owner=request.user, done=False, deadline__lt=datetime.date.today()
    ).order_by("-deadline"):
        if reminder.deadline not in overdue_reminders:
            overdue_reminders[reminder.deadline] = [reminder]
        else:
            overdue_reminders[reminder.deadline].append(reminder)

    for reminder in Reminder.objects.filter(owner=request.user, done=True).order_by(
        "-deadline"
    ):
        if reminder.deadline not in done_reminders:
            done_reminders[reminder.deadline] = [reminder]
        else:
            done_reminders[reminder.deadline].append(reminder)
    return render(
        request,
        "reminders.html",
        {
            "responseform": ReminderForm(),
            "reminders": reminder_by_date,
            "overdue_reminders": overdue_reminders,
            "done_reminders": done_reminders,
        },
    )


# delete reminder
def delete_reminder(request, reminder_id):
    reminder = Reminder.objects.get(id=reminder_id)
    reminder.delete()
    return redirect("reminders")


# done reminder
def done_reminder(request, reminder_id):
    reminder = Reminder.objects.get(id=reminder_id)
    reminder.done = True
    reminder.save()
    expense = Expense(
        amount=reminder.amount,
        date=datetime.date.today(),
        description=reminder.description,
        category=reminder.category,
        owner=reminder.owner,
    )
    expense.save()
    return redirect("reminders")
