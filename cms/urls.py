from django.conf.urls import url
from cms import views

urlpatterns = [
    # 書籍
    url(r'^task/$', views.task_list, name='task_list'),
    url(r'^task/add/$', views.task_edit, name='task_add'),
    url(r'^task/mod/(?P<task_id>\d+)/$', views.task_edit, name='task_mod'),
    url(r'^task/del/(?P<task_id>\d+)/$', views.task_delete, name='task_del'),
]
