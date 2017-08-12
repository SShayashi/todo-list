from django.db import models

# Create your models here.


class Task(models.Model):
    """Task"""
    name = models.CharField('TaskName', max_length=255)
    content = models.CharField('TaskContent', max_length=255)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Comment"""
    task = models.ForeignKey(Task, verbose_name='Task', related_name='Comments')
    comment = models.TextField('comment', blank=True)

    def __str__(self):
        return self.comment
