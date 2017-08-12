from django.forms import ModelForm
from cms.models import Task


class TaskForm(ModelForm):
    """Task form"""
    class Meta:
        model = Task
        fields = ('name', 'content')