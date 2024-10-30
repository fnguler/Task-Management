from .models import models, Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.forms import DateInput, ModelForm
from django import forms
from django.forms.widgets import PasswordInput, EmailInput, TextInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=PasswordInput())

class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project_id_fk', 'assigned_user_id_fk', 
                  'status', 'priority', 'due_date',]
        exclude = ['reporter_id_fk','created_at', 'updated_at',]
        widgets = {'due_date': forms.DateInput(attrs={'type': 'date'})}
