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
                  'cms/home.html',     # 使用するテンプレート
                  {'lists': todo_list})         # テンプレートに渡すデータ


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
    """タスク一覧"""
    todo_lists = TodoList.objects.all().order_by('id')
    todo_list = get_object_or_404(TodoList, pk=list_id)
    tasks = todo_list.Tasks.all()
    return render(request,
                  'cms/home.html',     # 使用するテンプレート
                  {'lists': todo_lists,
                   'tasks': tasks,
                   'list': todo_list})         # テンプレートに渡すデータ


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
    """タスクの編集"""
    if task_id:   # task_id が指定されている (修正時)
        todo_list = get_object_or_404(TodoList, pk=list_id)
        task = todo_list.Tasks.get(pk=task_id)
        task.is_completed = True
        task.save()
        return redirect('cms:task_list', list_id)
    else:         # task_id が指定されていない (追加時)
        return redirect('cms:task_list', list_id)
    #
    # if request.method == 'POST':
    #     form = TaskForm(request.POST, instance=task)  # POST された request データからフォームを作成
    #     if form.is_valid():    # フォームのバリデーション
    #         task = form.save(commit=False)
    #         task.save()
    #         return redirect('cms:task_list', list_id=list_id)
    # else:    # GET の時
    #     form = TaskForm(instance=task)  # task インスタンスからフォームを作成
    #
    # return render(request, 'cms/task_edit.html', dict(form=form, task_id=task_id, list_id=list_id))


def task_delete(request, list_id, task_id):
    """タスクの削除"""
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('cms:task_list', list_id)


class CommentList(ListView):
    """感想の一覧"""
    context_object_name='comment'
    template_name='cms/comment_list.html'
    paginate_by = 2  # paging 2 tasks in a page

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['task_id'])  # 親の書籍を読む
        comment = task.Comments.all().order_by('id')# 書籍の子供の、感想を読む
        self.object_list = comment

        context = self.get_context_data(object_list=self.object_list, task=task)
        return self.render_to_response(context)


def comment_edit(request, task_id, comment_id=None):
    """感想の編集"""
    task = get_object_or_404(Task, pk=task_id)  # 親の書籍を読む
    if comment_id:      # comment_id が指定されている (修正時)
        comment = get_object_or_404(Comment, pk=comment_id)
    else:               # comment_id が指定されていない (追加時)
        comment = Comment()

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            comment = form.save(commit=False)
            comment.task = task  # この感想の、親の書籍をセット
            comment.save()
            return redirect('cms:comment_list', task_id=task_id)
    else:    # GET の時
        form = CommentForm(instance=comment)  # comment インスタンスからフォームを作成

    return render(request,
                  'cms/comment_modify.html',
                  dict(form=form, task_id=task_id, comment_id=comment_id))


def comment_del(request, task_id, comment_id):
    """感想の削除"""
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('cms:comment_list', task_id=task_id)
