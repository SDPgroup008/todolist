from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('add_task/', views.add_task, name='add_task'),
     path('', views.task_list, name='task_list'),
]
