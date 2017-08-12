from django.shortcuts import render


from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Task


def task_list(request):
    """タスク一覧"""
    # return HttpResponse('list')
    tasks = Task.objects.all().order_by('id')
    return render(request,
                  'cms/task_list.html',     # 使用するテンプレート
                  {'tasks': tasks})         # テンプレートに渡すデータ


def task_add(request):
    """タスク追加"""
    return HttpResponse('add')


def task_edit(request, book_id=None):
    """タスクの編集"""
    return HttpResponse('edit')


def task_delete(request, book_id):
    """タスクの削除"""
    return HttpResponse('delete')