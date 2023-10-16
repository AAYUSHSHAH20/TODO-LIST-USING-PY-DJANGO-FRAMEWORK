from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from .forms import UserCreateForm,TaskForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginaccount(request):
        if request.method == 'GET':
                return render(request,'base/login.html',{'form':AuthenticationForm})
        else:
                user = authenticate(request,
                    username = request.POST['username'],
                    password = request.POST['password']
                    )
                if user is None:
                        return render(request,'base/login.html',{'form':AuthenticationForm,'error':'username and password does not match'})
                else:
                        login(request,user)
                        return redirect('tasks')


def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'base/register.html', 
                       {'form':UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], 
                            password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'base/register.html', 
                 {'form':UserCreateForm,
                 'error':'Username already taken. Choose new username.'})
        else:
            return render(request, 'base/register.html', 
             {'form':UserCreateForm, 'error':'Passwords do not match'})
 
# context_object_name = to change name of the context in html file
# template_name = to change name of the template(html file name)

def logoutaccount(request):
        logout(request)
        return redirect('login')       


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    count = tasks.filter(complete=False).count()
    search_input = request.GET.get('search-area', '')
    if search_input:
        tasks = tasks.filter(title__icontains=search_input)
    context = {
        'tasks': tasks,
        'count': count,
        'search_input': search_input,
    }
    return render(request, 'base/task_list.html', context)    
    
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    context = {
        'form': form,
    }
    return render(request, 'base/task_form.html', context)
    

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'base/task_form.html', {'form': form, 'task': task})    
    
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return render(request, 'base/task_confirm_delete.html', {'task': task})
    
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'base/task_detail.html', {'task': task})

def custom_404_view(request, exception=None):
    return render(request, 'base/404.html', status=404)    
    
    














#  r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'