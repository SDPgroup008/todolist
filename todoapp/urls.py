
from django.urls import path
from . import views

urlpatterns=[
    path('',views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('index/', views.homepage, name='index'),
    
    path('logout/', views.logout_view, name='logout'),
   
]