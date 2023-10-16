from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.models import User 
from .models import Task


class UserCreateForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):        
        super(UserCreateForm, self).__init__(*args,**kwargs)        
        for fieldname in ['username', 'password1','password2']:           
            self.fields[fieldname].help_text = None            
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'complete')            