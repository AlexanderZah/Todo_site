from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodosForm
from .models import Todos
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'todo/home.html')



def signupuser(request):
    """Представление регистрации пользователя"""
    if request.method == 'GET':
    
        return render(request,'todo/signupuser.html', context={'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request,'todo/signupuser.html', context={'form':UserCreationForm(), 'error':'That username has already been taken.Please choose a new username.',})
        else:
            return render(request,'todo/signupuser.html', context={'form':UserCreationForm(), 'error':'password did not match',})

def loginuser(request):
    """Представление входа пользователя"""
    if request.method == 'GET':
        return render(request,'todo/loginuser.html', context={'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'todo/loginuser.html', context={'form':AuthenticationForm(), 'error':'login or password did not match',})
        else:
            login(request, user)
            return redirect('currenttodos')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')            

@login_required
def currenttodos(request):
    """Представления для отображения задач todo"""
    todos = Todos.objects.filter(user=request.user, date_completed__isnull=True).order_by('-created')
    return render(request, 'todo/currenttodos.html', context={'todos':todos})

@login_required    
def completedtodos(request):
    """Представления для отображения выполненных задач todo"""
    todos = Todos.objects.filter(user=request.user, date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'todo/completedtodos.html', context={'todos':todos})


@login_required
def createtodo(request):
    """Представление для создание задач в форме"""
    if request.method == 'POST':
        try:
            form_todos = TodosForm(request.POST)
            newform =  form_todos.save(commit=False)
            newform.user = request.user
            newform.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request,'todo/createtodo.html',context={'form':TodosForm(), "error":"Bad data now. Try again.",})
    else:
        return render(request,'todo/createtodo.html',context={'form':TodosForm()})

@login_required
def edittodo(request, todo_id):
    """Представления для редактирования задачи todo"""
    todo = get_object_or_404(Todos, id=todo_id, user=request.user)
    if request.method == 'GET':
        form = TodosForm(instance=todo)
        return render(request, 'todo/edit_todo.html', context={'todo':todo, 'form':form})
    else:
        try:
            form = TodosForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/edit_todo.html', context={'todo':todo, 'form':form, 'error':'Bad data. Try again:)'})

@login_required
def completetodo(request,todo_id):
    """Функция выполнения задачи"""
    todo = get_object_or_404(Todos, id=todo_id, user=request.user)
    if request.method == 'POST':
        
        todo.date_completed = timezone.now()
        todo.save()
        return redirect('currenttodos')

@login_required
def deletetodo(request, todo_id):
    todo = get_object_or_404(Todos, id=todo_id, user=request.user)
    if request.method == 'POST':
        
        
        todo.delete()
        return redirect('currenttodos')