from django.shortcuts import render


from django.shortcuts import render
from django.http import HttpResponse


def task_list(request):
    """タスク一覧"""
    return HttpResponse('タスクの一覧')


def task_edit(request, book_id=None):
    """タスクの編集"""
    return HttpResponse('タスクの編集')


def task_delete(request, book_id):
    """タスクの削除"""
    return HttpResponse('タスクの削除')