from django.shortcuts import render, redirect
from .models import Tasks


def home_page(request):
    return render(request, 'index.html')

def get_task(request):
    task = Tasks.objects.all()
    return render(request, 'profile.html', {'task': task})




def add_task(request):
    if request.method == 'POST':
        Tasks.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            due_date=request.POST['due_date'],
            priority=request.POST['priority']
        )
        return redirect('show_task')

    return render(request, 'add_task.html')

def delete_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return redirect('show_task')



def complete_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.status = True
    task.save()
    return redirect('show_task')


def edit_task(request, task_id):
    task = Tasks.objects.get(id=task_id)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']
        task.priority = request.POST['priority']

        task.save()
        return redirect('show_task')

    return render(request, 'edit_task.html', {'task': task})