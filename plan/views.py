from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponse
from django.template.loader import render_to_string
import tempfile

# Create your views here.


def registartionPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'plan/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR Password is incorrect')
        context = {}
        return render(request, 'plan/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def homePage(request):
    plany = Plan.objects.filter(user=request.user)
    return render(request, 'plan/home.html', {'plany':plany})

@login_required(login_url='login')
def createTimetable(request):
    user = User.objects.get(id=request.user.id)
    form = PlanForm(initial={'user': user})
    name = 'Create'
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'name':name}
    return render(request, 'plan/plan_form.html', context)

@login_required(login_url='login')
def updateTimetable(request, pk):
    try:
        plan = Plan.objects.get(id=pk)
    except Plan.DoesNotExist:
        return redirect('home')
    if plan.user != request.user:
        return redirect('home')
    form = PlanForm(instance=plan)
    name = 'Update'
    if request.method == "POST":
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form, 'name': name}
    return render(request, 'plan/plan_form.html', context)

@login_required(login_url='login')
def deleteTimetable(request,pk):
    try:
        plan = Plan.objects.get(id=pk)
    except Plan.DoesNotExist:
        return redirect('home')
    if plan.user != request.user:
        return redirect('home')
    if request.method == 'POST':
        plan.delete()
        return redirect('home')
    context={'item':plan}
    return render(request, 'plan/plan_delete.html',context)

@login_required(login_url='login')
def timetableGeneralView(request, pk):
    dni= ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
    godziny =['8:00','8:15','8:30','8:45','9:00','9:15','9:30','9:45','10:00','10:15','10:30','10:45','11:00','11:15','11:30','11:45','12:00','12:15','12:30','12:45','13:00','13:15','13:30','13:45','14:00','14:15','14:30','14:45','15:00','15:15','15:30','15:45','16:00','16:15','16:30','16:45','17:00','17:15','17:30','17:45','18:00','18:15','18:30','18:45','19:00','19:15','19:30','19:45','20:00']
    try:
        plan = Plan.objects.get(id=pk)
    except Plan.DoesNotExist:
        return redirect('home')
    if plan.user != request.user:
        return redirect('home')
    lekcje = Lekcja.objects.filter(plan=plan)
    context={'lekcje':lekcje,'plan':plan,'dni':dni,'godziny':godziny}
    return render(request, 'plan/plan_main.html', context)

@login_required(login_url='login')
def createClass(request,pk):
    try:
        plan = Plan.objects.get(id=pk)
    except Plan.DoesNotExist:
        return redirect('home')
    if plan.user != request.user:
        return redirect('home')
    form = LekcjaForm(initial={'plan': plan})
    plano = plan.id
    name = 'Create Class'
    if request.method == "POST":
        form = LekcjaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable_view',pk)
    context = {'form': form, 'name':name, 'plan': plano}
    return render(request, 'plan/lekcja_form.html', context)

@login_required(login_url='login')
def deleteClass(request,pk):
    try:
        lekcja = Lekcja.objects.get(id=pk)
    except Lekcja.DoesNotExist:
        return redirect('home')
    plan = lekcja.plan.id
    plano = lekcja.plan.user
    if plano != request.user:
        return redirect('home')
    if request.method == 'POST':
        lekcja.delete()
        return redirect('timetable_view', plan)
    context={'item':lekcja, 'plan':plan }
    return render(request, 'plan/lekcja_delete.html',context)

@login_required(login_url='login')
def updateClass(request, pk):
    try:
        lekcja = Lekcja.objects.get(id=pk)
    except Lekcja.DoesNotExist:
        return redirect('home')
    plan = lekcja.plan.id
    plano = lekcja.plan.user
    if plano != request.user:
        return redirect('home')
    form = LekcjaForm(instance=lekcja)
    name = 'Update Class'
    if request.method == "POST":
        form = LekcjaForm(request.POST, instance=lekcja)
        if form.is_valid():
            form.save()
            return redirect('timetable_view', plan)
    context={'form':form, 'name': name, 'plan':plan}
    return render(request, 'plan/lekcja_form.html', context)

@login_required(login_url='login')
def render_to_pdf(request,pk):
    dni = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    godziny = ['8:00', '8:15', '8:30', '8:45', '9:00', '9:15', '9:30', '9:45', '10:00', '10:15', '10:30', '10:45',
               '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30',
               '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45', '16:00', '16:15',
               '16:30', '16:45', '17:00', '17:15', '17:30', '17:45', '18:00', '18:15', '18:30', '18:45', '19:00',
               '19:15', '19:30', '19:45', '20:00']
    try:
        plan = Plan.objects.get(id=pk)
    except Plan.DoesNotExist:
        return redirect('home')
    if plan.user != request.user:
        return redirect('home')
    lekcje = Lekcja.objects.filter(plan=plan)
    context = {'lekcje': lekcje, 'plan': plan, 'dni': dni, 'godziny': godziny}

    return render(request, 'plan/clear_table.html', context)
