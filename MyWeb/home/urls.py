from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/',  views.Regestration, name="Regestration"),
    path('login/', views.login, name="login_1")
   
]
