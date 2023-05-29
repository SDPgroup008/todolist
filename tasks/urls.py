from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('tasklist/', views.task_list, name='tasklist'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update_task_completion/', views.update_task_completion, name='update_task_completion'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('events/', views.load_events, name='load_events'),
    
]
