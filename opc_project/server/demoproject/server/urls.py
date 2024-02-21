from django.urls import path
from . import views

urlpatterns = [
    path('start-server', views.start_opcua, name='start_opcua'),
    path('register-users', views.register_users, name='register_users'),
    path('login-user', views.login_user, name='login_user'),
]