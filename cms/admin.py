from django.contrib import admin

from cms.models import TodoList, Task, Comment

admin.site.register(TodoList)
admin.site.register(Task)
admin.site.register(Comment)