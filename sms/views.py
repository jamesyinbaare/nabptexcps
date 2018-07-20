from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'sms/dashboard_index.html', {'greet': 'hello world'})



def manage_students(request):

    return render(request, 'sms/dashboard_manage_students.html',{})
