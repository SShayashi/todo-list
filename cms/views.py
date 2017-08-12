from django.shortcuts import render


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from cms.models import Task
from cms.forms import TaskForm


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


def task_edit(request, task_id=None):
    """タスクの編集"""
    if task_id:   # task_id が指定されている (修正時)
        task = get_object_or_404(Task, pk=task_id)
    else:         # task_id が指定されていない (追加時)
        task = Task()

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            task = form.save(commit=False)
            task.save()
            return redirect('cms:task_list')
    else:    # GET の時
        form = TaskForm(instance=task)  # task インスタンスからフォームを作成

    return render(request, 'cms/task_edit.html', dict(form=form, task_id=task_id))

    return HttpResponse('edit')


def task_delete(request, task_id):
    """タスクの削除"""
    return HttpResponse('delete')