import json
from django.shortcuts import render, HttpResponse

from django.shortcuts import render, redirect
from django.db.models import Count, Sum, Q, OuterRef
from django.contrib.auth import authenticate, login, logout
from .models import Expense, Category, Reminder, Budget, Card
from .forms import (
    SignupForm,
    LoginForm,
    ExpenseForm,
    CategoryForm,
    ReminderForm,
    BudgetForm,
    CardForm
)

import datetime
import pytesseract
from PIL import Image
import dateutil.parser
import re

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
            ).order_by("-createdon") | Expense.objects.filter(owner=request.user).filter(
                category__name__icontains=searchbox_main
            ).order_by(
                "-createdon"
            ):
                if expense.createdon not in expenses_by_date:
                    expenses_by_date[expense.createdon] = [expense]
                else:
                    expenses_by_date[expense.createdon].append(expense)
    else:
        for expense in Expense.objects.filter(owner=request.user).order_by("-createdon"):
            if expense.createdon not in expenses_by_date:
                expenses_by_date[expense.createdon] = [expense]
            else:
                expenses_by_date[expense.createdon].append(expense)
    
    try:
        left_to_use = (
                Budget.objects.filter(owner=request.user).first().amount
                - Expense.objects.filter(owner=request.user).aggregate(Sum("amount"))[
                    "amount__sum"
                ]
                if Budget.objects.filter(owner=request.user).first()
                else 0
            )
    except:
        left_to_use = Budget.objects.filter(owner=request.user).first().amount

    expenseform = ExpenseForm()
    expenseform.fields["paymentMethod"].widget.attrs["default"] = "Cash"
    return render(
        request,
        "index.html",
        {
            "expenseform": expenseform,
            "expenses": expenses_by_date,
            "allexpenses": Expense.objects.filter(owner=request.user).order_by("-createdon"),
            "categories": Category.objects.annotate(
                count=Count("expense"),
                total_amount=Sum("expense__amount"),
            ),
            "budget": Budget.objects.filter(owner=request.user).first(),
            "left_to_use": left_to_use,
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

# modify address page
def modify_address(request):
    if request.method == "POST":
        req = json.loads(request.body)
        address = req.get('address')
        expenseid = req.get('expenseid')
        if not expenseid:
            return HttpResponse('failed')
        expense = Expense.objects.get(id=expenseid)
        expense.address = address
        expense.save()
        return HttpResponse('success')

# logout page
def user_logout(request):
    logout(request)
    return redirect("login")

# create expense page
def create_expense(request):
    if request.method == "POST":
        recieptImage = None
        for filename, file in request.FILES.items():
            recieptImage = request.FILES.get(filename)
        if recieptImage:
            recieptImage = Image.open(recieptImage)
            category = request.POST.get("category")
            recieptImage = pytesseract.image_to_string(recieptImage)
            total, date = 0, None
            for i in recieptImage.split("\n"):
                if 'total' in i.lower():
                    total = float(re.sub('[^0-9,.]', '', i))
                if 'date' in i.lower():
                    date = dateutil.parser.parse(i.lower().replace("date", "").lstrip(":").replace(" ", ""))
                if total and date:
                    break
            if (not total) or (not date):
                recieptImage = None

        if recieptImage:
            expense = Expense(
                amount=total,
                createdon=date,
                description='',
                category=Category.objects.get(name=category),
                owner=request.user,
            )
            expense.save()
            return redirect("home")
        
        if not recieptImage:
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
                total_amount=Sum("expense__amount", filter=Q(expense__owner=request.user)),
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
        createdon=datetime.date.today(),
        description=reminder.description,
        category=reminder.category,
        owner=reminder.owner,
    )
    expense.save()
    return redirect("reminders")


# budget page
def budget(request):
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            budget = Budget.objects.filter(owner=request.user).first()
            if budget:
                budget.amount = form.amount
                budget.save()
            else:
                form.owner = request.user
                form.save()            
            return redirect("budget")
    return render(
        request,
        "set_budget.html",
        {
            "budget_form": BudgetForm(),
            "current_budget": Budget.objects.filter(owner=request.user).first(),
        },
    )


# graphs page
def graph(request):
    expense_current_month_ = (
        Expense.objects.filter(
            owner=request.user,
            createdon__gte=datetime.date.today() - datetime.timedelta(days=30),
        )
        .annotate(amount_=Sum("amount"))
        .order_by("createdon")
    )
    category_current_month_ = (
        Expense.objects.filter(
            owner=request.user,
            createdon__gte=datetime.date.today() - datetime.timedelta(days=30),
        )
        .values("category")
        .annotate(amount_=Sum("amount"))
        .order_by("amount_")
    )
    count_per_category_current_month_ = (
        Expense.objects.filter(
            owner=request.user,
            createdon__gte=datetime.date.today() - datetime.timedelta(days=30),
        )
        .values("category")
        .annotate(count=Count("category"))
    )
    count_per_payment_method_current_month_ = (
        Expense.objects.filter(
            owner=request.user,
        )
        .values("paymentMethod")
        .annotate(count=Count("paymentMethod"), payment_method=Card.objects.filter(id=OuterRef("paymentMethod")).values("name"))
    )
    count_per_payment_method_current_month = {}
    for i in count_per_payment_method_current_month_:
        count_per_payment_method_current_month[(lambda x: x if x else 'Cash')(i["payment_method"])] = i["count"]
    if count_per_payment_method_current_month.get('Cash') is not None:
        count_per_payment_method_current_month['Cash'] += 1
    return render(
        request,
        "graphs.html",
        {
            "expense_current_month": [
                {"day": i.createdon.strftime("%d %b %Y"), "expense": i.amount_}
                for i in expense_current_month_
            ],
            "category_current_month": [
                {"category": Category.objects.get(id=i["category"]).name, "expense": i["amount_"]}
                for i in category_current_month_
            ],
            "count_per_category_current_month": [
                {"category": Category.objects.get(id=i["category"]).name, "count": i["count"]}
                for i in count_per_category_current_month_
            ],
            "count_per_payment_method_current_month": [
                {"payment_method": k, "count": v}
                for k, v in count_per_payment_method_current_month.items()
            ],
        },
    )

def cards(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            return redirect("card")
    
    return render(request, "cards.html", {"cards": Card.objects.annotate(count=Count("expense"), total_amount=Sum("expense__amount", filter=Q(expense__owner=request.user))), "cardform": CardForm()})

def delete_card(request, card_id):
    card = Card.objects.get(id=card_id)
    card.delete()
    return redirect("/card")