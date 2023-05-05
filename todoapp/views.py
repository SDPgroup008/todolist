from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import Task
 

# Create your views here.

def homepage(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'home.html', context)

# def homepage(request):
#     return render(request,'home.html')


def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username or password is incorrect !!")



    return render(request, 'login.html')
    


def signup_page(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')


    return render(request, 'signup.html')



def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task = Task.objects.create(title=title, description=description)
        return redirect('tasks:home')

