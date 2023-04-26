
from django.urls import path
from . import views

urlpatterns=[
    
    path('', views.signup, name='signup'),
    path('login/',views.user_login, name='login'),
    path('home/', views.homepage, name='home'),
    path('logut/', views.Logoutpage, name='logout')
]