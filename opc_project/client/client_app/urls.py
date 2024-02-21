from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('node/', views.select_node, name="select_node"),
]