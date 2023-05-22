from django.shortcuts import render, redirect
from .models import Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import TaskForm
from .models import Event

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

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasklist.html', {'tasks': tasks})



def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.completed = request.POST.get('completed', False)
        task.save()
        return redirect('tasks:tasklist')
    
    context = {'task': task}
    return render(request, 'edit_task.html', context)


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
    


# def calendar_view(request):
#     return render(request, 'calendar.html')

# def load_events(request):
#     events = Event.objects.all()
#     data = []
#     for event in events:
#         data.append({
#             'title': event.title,
#             'start': event.start_datetime.isoformat(),
#             'end': event.end_datetime.isoformat(),
#         })
#     return JsonResponse(data, safe=False)
