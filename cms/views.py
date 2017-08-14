from django.shortcuts import render


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView

from cms.models import TodoList, Task, Comment
from cms.forms import TaskForm, CommentForm


def handle_page_not_found(request):
    return redirect('cms:home')


def all_list(request):
    todo_list = TodoList.objects.all().order_by('id')
    return render(request,
                  'cms/home.html',
                  {'lists': todo_list})


def list_add(request):
    if request.method == 'POST':
        todo_list = TodoList()
        todo_list.name = request.POST['list_name']
        todo_list.save()
        return redirect('cms:home')
    else:
        return redirect('cms:home')


def list_delete(request, list_id):
    """delete list"""
    todo_list = get_object_or_404(TodoList, pk=list_id)
    todo_list.delete()
    return redirect('cms:home')


def task_list(request, list_id):
    """task list"""
    todo_lists = TodoList.objects.all().order_by('id')
    todo_list = get_object_or_404(TodoList, pk=list_id)
    tasks = todo_list.Tasks.all()
    return render(request,
                  'cms/home.html',
                  {'lists': todo_lists,
                   'tasks': tasks,
                   'list': todo_list})


def task_add(request, list_id):

    if request.method == 'POST':
        task = Task()
        task.list_id = list_id
        task.name = request.POST['task_name']
        task.save()
        return redirect('cms:task_list', list_id)
    else:
        return redirect('cms:task_list', list_id)


def task_edit(request, list_id, task_id=None):
    """edit task"""
    if task_id:
        todo_list = get_object_or_404(TodoList, pk=list_id)
        task = todo_list.Tasks.get(pk=task_id)
        task.is_completed = True
        task.save()
        return redirect('cms:task_list', list_id)
    else:
        return redirect('cms:task_list', list_id)


def task_delete(request, list_id, task_id):
    """delete task"""
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('cms:task_list', list_id)
