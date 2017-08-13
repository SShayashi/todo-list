from django.db import models

# Create your models here.


class TodoList(models.Model):
    name = models.CharField('ListName', max_length=255, default='NewList')

    def __str__(self):
        return self.name


class Task(models.Model):
    """Task"""
    list = models.ForeignKey(TodoList, verbose_name='TodoList', related_name='Tasks')
    name = models.CharField('TaskName', max_length=255)
    content = models.CharField('TaskContent', max_length=255)
    is_completed = models.BooleanField('is_completed', default=False)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Comment"""
    task = models.ForeignKey(Task, verbose_name='Task', related_name='Comments')
    comment = models.TextField('comment', blank=True)

    def __str__(self):
        return self.comment
