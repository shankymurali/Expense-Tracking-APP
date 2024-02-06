from django.db import models

# Create your models here.

class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    description = models.TextField(max_length=1024)
    owner = models.ForeignKey('auth.User', related_name='expenses', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

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