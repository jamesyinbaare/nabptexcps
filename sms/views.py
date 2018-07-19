from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'sms/dashboard_index.html', {'greet': 'hello world'})