
from django.urls import include, path
from . import views

urlpatterns=[
    path('',views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('home/', views.homepage, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    # path('tasks/', include('tasks.urls', namespace='tasks'))
]