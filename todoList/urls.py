from django.urls import re_path
from todoList import views


urlpatterns=[
    re_path(r'^list$', views.listApi),
    re_path(r'^list/([0-9]+)$', views.listApi),

    re_path(r'^task$', views.taskApi),
    re_path(r'^task/([0-9]+)$', views.taskApi),
    re_path(r'^task/from/([0-9]+)$', views.taskByList)
]