from django.conf.urls import url
from cms import views

urlpatterns = [
    # 書籍
    url(r'^home/$', views.all_list, name='home'),
    url(r'^home/add/$', views.list_add, name='list_add'),
    url(r'^task/(?P<list_id>\d+)/$', views.task_list, name='task_list'),
    url(r'^task/add/(?P<list_id>\d+)/$', views.task_edit, name='task_add'),
    url(r'^task/mod/(?P<list_id>\d+)/(?P<task_id>\d+)/$', views.task_edit, name='task_mod'),
    url(r'^task/del/(?P<list_id>\d+)/(?P<task_id>\d+)/$', views.task_delete, name='task_del'),
    url(r'^comment/(?P<task_id>\d+)/$', views.CommentList.as_view(), name='comment_list'),
    url(r'^comment/add/(?P<task_id>\d+)/$', views.comment_edit, name='comment_add'),
    url(r'^comment/mod/(?P<task_id>\d+)/(?P<comment_id>\d+)/$', views.comment_edit, name='comment_mod'),
    url(r'^comment/del/(?P<task_id>\d+)/(?P<comment_id>\d+)/$', views.comment_del, name='comment_del'),
]
