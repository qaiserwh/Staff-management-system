
from.models import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from . forms import AdminLoginForm, AttendForm,TrainingForm, VacationForm
# Create your views here.
def index(request):
    search=Employ.objects.all()
    name= None
    if 'search_name'  in request.GET:
        name =request.GET['search_name']
        if name:
            search = search.filter(name__icontains=name)
    context ={
    'emp':search
    }
    return render(request,'pages/index.html',context)

def admin_login(request):
     forms = AdminLoginForm()
     if request.method == 'POST':
         forms = AdminLoginForm(request.POST)
         if forms.is_valid():
             username = forms.cleaned_data['username']
             password = forms.cleaned_data['password']
             user = authenticate(username=username, password=password)
             if user:
                 login(request,user)
                 return redirect('index')
     context = {'forms': forms}
     return render(request,'pages/login.html', context)




def info(request):
    context={
        'photo':Employ.objects.all()
    }
    return render(request,'pages/info.html',context)

def Admin(request):
    return render


def attendance(request):
    search=Attendance.objects.all()
    status= None
    if 'search_name'  in request.GET:
        status =request.GET['search_name']
        if status:
            search = search.filter(status__icontains=status)
    context ={
    'em':search
    }
    return render(request,'pages/attendance.html',context)
    
def addatt(request):
    if request.method =='POST':
        Att= AttendForm(request.POST)
        if Att.is_valid():
            Att.save()
            return  redirect('Attendance')

    context ={
        'name_employ': Attendance.objects.all(),
        'forms': AttendForm(),
        'status':Attendance.objects.all(),
        'date':Attendance.objects.all()
    }
    return render(request,'pages/addatt.html',context)

def addveca(request):
    if request.method =='POST':
        Att= VacationForm(request.POST)
        if Att.is_valid():
            Att.save()
            return  redirect('vacation')

    context ={
        'employ_name': Vacation.objects.all(),
        'forms': VacationForm(),
        'title':Vacation.objects.all(),
        'start_date':Vacation.objects.all(),
        'end_date':Vacation.objects.all(),
        'purpose':Vacation.objects.all()
    }
    return render(request,'pages/addveca.html',context)   

def addtraning(request):
    if request.method =='POST':
        Att= TrainingForm(request.POST)
        if Att.is_valid():
            Att.save()
            return  redirect('Trainings')

    context ={
        'names': Attendance.objects.all(),
        'forms': TrainingForm(),
        'title':Training.objects.all(),
        'description':Training.objects.all()
    }
    return render(request,'pages/addtraning.html',context)


def vac(request):
    context={
        'emr':Vacation.objects.all()
    }
    return render(request,'pages/vacation.html',context)
def tran(request):
    context={
        'eml':Training.objects.all()
    }
    return render(request,'pages/trainings.html',context)
