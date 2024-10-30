import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.context_processors import csrf
from taskmanagement.forms import LoginForm, CreateUserForm, CreateTaskForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .models import Task


def home(request):
    if request.user.is_authenticated:
        return redirect("board")
    else:
        return render(request, 'taskmanagement/home.html')

def login(request):
    loginForm = LoginForm()
    registerForm = CreateUserForm()

    if request.method == "POST":
        if 'loginForm_submit' in request.POST:
            loginForm = LoginForm(request, data=request.POST)
            if loginForm.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    auth.login(request,user)
                    return redirect("board")
        elif 'registerForm_submit' in request.POST:
            registerForm = CreateUserForm(request.POST)
            if registerForm.is_valid():
                registerForm.save()
                return redirect('login')
    context = {'loginForm': loginForm,
    'registerForm': registerForm}
    return render(request, 'taskmanagement/login.html',  context=context)


def logout(request):
    auth.logout(request)
    return redirect("login")

@login_required(login_url='login')
def board(request):
    currentUser = request.user.id    
    can_create_task = request.user.has_perm('taskmanagement.add_task')
    tasksTodo = Task.objects.filter(assigned_user_id_fk=currentUser, status='todo')
    tasksInProgress = Task.objects.filter(assigned_user_id_fk=currentUser, status='in-progress')
    tasksDone = Task.objects.filter(assigned_user_id_fk=currentUser, status='done')

    if request.method == 'POST':
        createTaskForm = CreateTaskForm(request.POST)
        if createTaskForm.is_valid():
            task = createTaskForm.save(commit=False)
            task.reporter_id_fk = request.user
            task.save()
            return redirect("board")
        else:
            return redirect("board")
    createTaskForm = CreateTaskForm()

    context = {'createTaskForm': createTaskForm,
                'tasksToDo':tasksTodo,
                'tasksInProgress':tasksInProgress,
                'tasksDone':tasksDone,
                'can_create_task':can_create_task,}
    return render(request, 'taskmanagement/board.html', context=context)

@login_required(login_url='login')
def viewTask(request, task_id):
    return redirect('board')

@login_required(login_url='login')
def updateTask(request, task_id):
    can_delete_task = request.user.has_perm('taskmanagement.delete_task')
    can_update_task = request.user.has_perm('taskmanagement.change_task')
    task = Task.objects.get(id=task_id)
    createTaskForm = CreateTaskForm(instance=task)
    if request.method == 'POST':
        if 'updateTask' in request.POST:
            createTaskForm = CreateTaskForm(request.POST, instance=task)
            if createTaskForm.is_valid():
                createTaskForm.save()
                return redirect('board')
        elif 'deleteTask' in request.POST:
            task.delete()
            return redirect('board')
    context = {'createTaskForm':createTaskForm,
    'can_update_task':can_update_task,
    'can_delete_task':can_delete_task,}
    return render(request,'taskmanagement/update-task.html', context=context)

@login_required(login_url='login')
def deleteTask(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('board')
    return render(request,'taskmanagement/delete-task.html')
