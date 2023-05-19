from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.contrib.auth import authenticate,login

 

# Create your views here.

# def homepage(request):
#     tasks = Task.objects.all()
#     context = {'tasks': tasks}
#     return render(request, 'home.html', context)

def homepage(request):
     return render(request,'home.html')


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
    

=======
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
 

# Create your views here.
@login_required(login_url='login')
def homepage(request):
    return render(request, 'home.html')
>>>>>>> 76db4f5fb68890858bfe67da8b0489ebcc2fd697

def signup_page(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')


    return render(request, 'signup.html')




<<<<<<< HEAD
=======
def user_login(request):
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
    





def Logoutpage(request):
    logout(request)
    return redirect('login')

>>>>>>> 76db4f5fb68890858bfe67da8b0489ebcc2fd697
