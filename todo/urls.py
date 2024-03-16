from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('mark_todo/<int:todo_id>/', views.mark_todo, name='mark_todo'),
]
