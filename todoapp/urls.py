
from django.urls import path
from . import views

urlpatterns=[
<<<<<<< HEAD
    path('',views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('home/', views.homepage, name='home'),
    # path('add_task/', views.add_task, name='add_task'),
    # path('tasks/', include('tasks.urls', namespace='tasks'))
=======
    
    path('', views.signup, name='signup'),
    path('login/',views.user_login, name='login'),
    path('home/', views.homepage, name='home'),
    path('logut/', views.Logoutpage, name='logout')
>>>>>>> 76db4f5fb68890858bfe67da8b0489ebcc2fd697
]