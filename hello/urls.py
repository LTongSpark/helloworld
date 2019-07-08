# -*- coding: utf-8 -*-
from django.urls import path,include
from . import views

urlpatterns = [
    path('index/' ,views.index),
    path('hello/' ,views.hello, name = "page_hello"),
    path('page/<int:num>/' ,views.page),
    path('home/<year>/<month>/' ,views.home),
    path('hello/demo/' ,views.demo ,name = "page_demo"),
    path('name/' ,views.name),
    path('add/' ,views.add),
    path('regist/' ,views.regist),
    path('update/',views.update),
    path('delete/' ,views.delete),
    path('select/' ,views.select),
    path('selectall/',views.select_all),
    path('json/' ,views.get_json),
    path('result/',views.result),
    path('qq/' ,views.test_qq),
    path('email/' ,views.user),
    path('register/' ,views.register),
    path('login/' ,views.login),
    path('reset/' ,views.reset_pwd),
    path('mail/' ,views.mail)

]