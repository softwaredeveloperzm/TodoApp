from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from .models import Task
import time


@login_required
def home(request):
    if request.method == "POST": 
        contents = request.POST['text']
        due_date = request.POST['date']
        
        username = request.user
        task = Task.objects.create(contents=contents, user=username, due_date=due_date)
        return redirect('home')

    username = request.user
    tasks = Task.objects.filter(user=username)
    upcoming_task = Task.objects.filter(completed=False, user=request.user)
    completed_task = Task.objects.filter(completed=True, user=request.user)


    context = {
        'tasks': tasks,
        'upcoming_task': upcoming_task,
        'completed_task': completed_task
    }

    return render(request, "main/home.html", context)


def delete_task(request, task_id):
    task = Task.objects.filter(id=task_id)

    task.delete()
    messages.success(request, "Task Deleted Succefully." )
    return redirect('home')

def update_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)
    task.contents = request.POST.get('text')
    # Save the updated task
    task.save()

    return redirect('home')


def register(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_password_confrim = request.POST.get('password_confrim')



        if User.objects.filter(username=user_email).exists():
            messages.warning(request, "Email already exists!")
            return redirect('register')

        elif user_password != user_password_confrim:
            messages.warning(request, "Password Does Not Macth!")
            return redirect('register')

        elif  user_password == user_email:
            messages.warning(request, "Password cannot be the same as the username.")
            return redirect('register')

        elif len(user_password) < 8:
            messages.warning(request, "Password must be at least 8 characters long.")
            return redirect('register')

        else:
            User.objects.create_user(username=user_email, password=user_password)
            messages.success(request, 'Account Created Succefully')
            time.sleep(10)
            return redirect('user_login')
        



    return render(request, 'main/register.html')

def user_login(request):
    if request.method == "POST":
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')


        user = authenticate(username=user_email, password=user_password)
        if user is not None:
            login(request, user)
            
            return redirect('home') 
        else:
            print("Login failed")
            return redirect('user_login') 

    return render(request, "main/login.html")

def logout_user(request):
    logout(request)
    return redirect('usel_login')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    
    return redirect('home')