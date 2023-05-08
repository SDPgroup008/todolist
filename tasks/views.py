from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def homepage(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'home.html', context)




# def add_task(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         description = request.POST['description']
#         task = Task.objects.create(title=title, description=description)
#         return redirect('tasks:home')
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:tasklist')
    else:
        form = TaskForm()
    return render(request, 'home.html', {'form': form})

def tasklist(request):
    tasks = Task.objects.all()
    return render(request, 'tasklist.html', {'tasks': tasks})
# Create your views here.
