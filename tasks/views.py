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
def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    # Handle form submission and update task
    if request.method == 'POST':
        # Process form data and update the task
        task.title = request.POST['title']
        task.save()
        return redirect('task_list')  # Redirect to the task list page
    
    context = {'task': task}
    return render(request, 'edit_task.html', context)

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    # Handle form submission and delete task
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Redirect to the task list page
    
    context = {'task': task}
    return render(request, 'delete_task.html', context)