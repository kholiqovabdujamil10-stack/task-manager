from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home'),
    path('tasks/', get_task, name='show_task'),
    path('add-task/', add_task, name='add_task'),
    path('delete-task/<int:task_id>/', delete_task, name='delete_task'),
    path('complete-task/<int:task_id>/', complete_task, name='complete_task'),
    path('edit-task/<int:task_id>/', edit_task, name='edit_task'),
]