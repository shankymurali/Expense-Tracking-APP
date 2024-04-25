import datetime
from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=266)
    cardnumber = models.CharField(max_length=266)
    cvc = models.CharField(max_length=266)
    expiry = models.DateField()
    description = models.TextField(max_length=1024)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} - {self.cardnumber}"

class Expense(models.Model):
    amount = models.FloatField()
    createdon = models.DateTimeField( default=datetime.datetime.now ) 
    description = models.TextField(max_length=1024)
    owner = models.ForeignKey('auth.User', related_name='expenses', on_delete=models.CASCADE)
    paymentMethod = models.ForeignKey('Card', on_delete=models.CASCADE, blank=True, null=True, default=None)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    address = models.CharField(max_length=1266, blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=266)

    def __str__(self):
        return self.name

class Reminder(models.Model):
    deadline = models.DateField()
    name = models.CharField(max_length=266)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField(max_length=1024)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='reminders', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ExpenseCollaborator(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    collaborator = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Budget(models.Model):
    amount = models.FloatField(default=0)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)