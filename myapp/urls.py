#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @date: 2020-06-01 
# @name: urls
# @author：shimengqi

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
]