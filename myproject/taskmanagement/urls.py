from django.urls import path
from . import views

#Define a list of url patterns

urlpatterns = [
    path('', views.home, name = "home"),
    path('login', views.login, name ="login"),
    path('logout', views.logout, name="logout"),
    path('board', views.board, name = "board"),
    path('update-task/<int:task_id>', views.updateTask, name='update-task'),
    path('delete-task/<int:task_id>', views.deleteTask, name='delete-task')
] 