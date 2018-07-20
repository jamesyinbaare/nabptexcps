from django.shortcuts import render
from . forms import StudentForm

# Create your views here.

def dashboard(request):
    return render(request, 'sms/dashboard_index.html', {'greet': 'hello world'})



def manage_students(request):

    return render(request, 'sms/dashboard_manage_students.html',{})


def add_student(request):
    
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    
    return render(request,'sms/add_student.html',{'form': form})