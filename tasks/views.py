from django.shortcuts import render, redirect
from .models import Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import TaskForm
from datetime import date, timedelta
from .models import Event
from datetime import datetime
from django.utils.timezone import make_aware

def homepage(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'home.html', context)

from django.shortcuts import render, redirect
from .forms import TaskForm

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            due_date = form.cleaned_data['due_date']
            due_time = form.cleaned_data['due_time']
            due_datetime = datetime.combine(due_date, due_time)
            task.due_datetime = make_aware(due_datetime)
            task.save()
            return redirect('tasks:tasklist')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})



def task_list(request):
    tasks = Task.objects.all()
    current_datetime = datetime.now()

    for task in tasks:
        remaining_time = task.due_datetime - current_datetime
        task.remaining_time = remaining_time

    return render(request, 'tasklist.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)

def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            due_date = form.cleaned_data['due_date']
            due_time = form.cleaned_data['due_time']
            due_datetime = datetime.combine(due_date, due_time)
            task.due_datetime = make_aware(due_datetime)
            task.save()
            return redirect('tasks:tasklist')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})




def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:tasklist')
    
    context = {'task': task}
    return render(request, 'delete_task.html', context)

def update_task_completion(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        task_id = request.POST.get('task_id')
        completed = request.POST.get('completed') == 'true'
        
        # Update the task completion status in the database
        
        return JsonResponse({'message': 'Task completion status updated successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)

def calendar_view(request):
    # Get the current date
    today = date.today()

    # Calculate the start and end dates for the calendar view
    start_date = today - timedelta(days=today.weekday())
    end_date = start_date + timedelta(days=6)

    # Generate a list of dates within the range
    calendar_dates = []
    current_date = start_date
    while current_date <= end_date:
        calendar_dates.append(current_date)
        current_date += timedelta(days=1)

    return render(request, 'calendar.html', {'dates': calendar_dates})

def load_events(request):
    events = Event.objects.all()
    data = []
    for event in events:
        data.append({
            'title': event.title,
            'start': event.start_datetime.isoformat(),
            'end': event.end_datetime.isoformat(),
        })
    return JsonResponse(data, safe=False)
