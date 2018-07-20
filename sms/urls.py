from django.urls import path
from . import views

app_name = 'sms'

urlpatterns = [
    path('',views.dashboard, name='dashboard' ),
    path('dashboard/students',views.manage_students, name='dashboard_manage_students' ),
    
]
