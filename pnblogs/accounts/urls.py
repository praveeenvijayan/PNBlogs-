from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from .views import usrReg


urlpatterns = [
   path('register/', usrReg.as_view(), name='register'),
] 