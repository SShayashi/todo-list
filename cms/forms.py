from django.forms import ModelForm
from cms.models import TodoList, Task, Comment


class TodoListForm(ModelForm):
    """Todo List Form"""
    class Meta:
        model = TodoList
        fields = ('name',)


class TaskForm(ModelForm):
    """Task form"""
    class Meta:
        model = Task
        fields = ('list', 'name', 'content')


class CommentForm(ModelForm):
    """感想のフォーム"""
    class Meta:
        model = Comment
        fields = ('comment', )