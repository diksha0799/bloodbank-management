from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name ="home"),
    path("registerhospital/", views.registerhospital, name ="registerhospital"),
    path("registerreciever/", views.registerreciever, name ="registerreciever"),
    path("login/", views.login, name ="login"),   
    path("hospital/", views.hospital, name="hospital"),
]
