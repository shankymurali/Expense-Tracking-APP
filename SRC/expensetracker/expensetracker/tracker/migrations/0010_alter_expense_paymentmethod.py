# Generated by Django 3.2.16 on 2024-04-07 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_expense_paymentmethod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='paymentMethod',
            field=models.ForeignKey(blank=True, default='Cash', null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.card'),
        ),
    ]
