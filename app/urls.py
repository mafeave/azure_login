
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_successful,name='login-view'),
    path('', views.register_user, name='register'),
    path('register/', views.register_user, name='register'),
]