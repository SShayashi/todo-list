from django.conf.urls import url
from cms import views

urlpatterns = [
    # 書籍
    url(r'^home/$', views.all_list, name='home'),
    url(r'^home/add/$', views.list_add, name='list_add'),
    url(r'^home/del/(?P<list_id>\d+)/$', views.list_delete, name='list_del'),
    url(r'^home/task/(?P<list_id>\d+)/$', views.task_list, name='task_list'),
    url(r'^home/task/add/(?P<list_id>\d+)/$', views.task_add, name='task_add'),
    url(r'^home/task/mod/(?P<list_id>\d+)/(?P<task_id>\d+)/$', views.task_edit, name='task_mod'),
    url(r'^home/task/del/(?P<list_id>\d+)/(?P<task_id>\d+)/$', views.task_delete, name='task_del'),
]
