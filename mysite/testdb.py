#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @date: 2020-06-02 
# @name: testdb
# @author：shimengqi
#
from django.http import HttpResponse

# from myapp.models import Stu
from myapp import models

from myapp.models import Person

def testdb(request):

    test1=Person(first_name='mengqi',last_name='shi')
    # test1=Stu(name='lily',age='18',sex='f',classid='3')
    test1.save()
    return HttpResponse("<p>数据添加成功</p>")

