from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('create-expense/', views.create_expense, name='create_expense'),
    path('delete-expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('manage-category/', views.manage_category, name='manage_category'),
    path('delete-category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('reminders/', views.reminder, name='reminders'),
    path('delete-reminder/<int:reminder_id>/', views.delete_reminder, name='delete_reminder'),
    path('done-reminder/<int:reminder_id>/', views.done_reminder, name='done_reminder'),
]