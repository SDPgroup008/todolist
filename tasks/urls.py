from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('add_task/', views.add_task, name='add_task'),
     path('task_list', views.task_list, name='task_list'),
]
