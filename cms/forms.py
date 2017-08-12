from django.forms import ModelForm
from cms.models import Task
from cms.models import Task, Comment


class TaskForm(ModelForm):
    """Task form"""
    class Meta:
        model = Task
        fields = ('name', 'content')


class CommentForm(ModelForm):
    """感想のフォーム"""
    class Meta:
        model = Comment
        fields = ('comment', )