
from django.urls import path
  
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path("login/" , views.loginaccount , name="login"),
    path("logout/" , views.logoutaccount , name="logout"),
    path("register/" , views.signupaccount , name="register"),
    path("" , views.task_list , name="tasks"),
    path("task-create/" , views.task_create , name="task-create"),
    path("task-update/<int:pk>/" , views.update_task , name="task-update"),
    path("task/<int:pk>/" , views.task_detail , name="task"),
    path("task-delete/<int:pk>/" , views.task_delete , name="task-delete"),
    path("task-detail/<int:pk>" , views.task_detail , name="task-detail"),
    
    
]
