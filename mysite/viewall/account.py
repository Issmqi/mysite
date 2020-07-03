#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
# @date: 2020-06-04 
# @name: account
# @author：shimengqi
'''

from django import views
from django.http import JsonResponse
from django.contrib import auth
from django.shortcuts import render, redirect, reverse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import UserInfo
from myapp.serializers import user_serializers
import json
from mysite.common.util import log

log = log.Log()


class Login(views.View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        data = request.POST  # a=1&b=2
        body = request.body

        param_str = str(body, encoding="utf-8")
        param_dict = eval(param_str)
        # param_data=json.loads(body)
        log.debug('param_dict的类型是%s' % type(param_dict))
        log.info('param_dict是%s' % param_dict)
        log.debug('data是%s' % data)
        log.debug('data的类型是%s' % type(data))
        log.debug('body的类型是%s' % type(body))
        log.info('body是%s' % body)
        username = param_dict['username']
        password = param_dict['password']
        # username = data.get("username")
        # password = data.get("password")
        log.info('用户名是%s' % username)
        log.info('密码是%s' % password)

        user = auth.authenticate(username=username, password=password)
        if user:
            # 将用户名存入session
            request.session['user'] = username
            auth.login(request, user)  # 将用户信息存入session
            result = {
                'code': 1,
                'status': 'success',
                'message': '登录成功'
            }

            return JsonResponse(result)
        else:
            result = {
                'code': 3,
                'status': 'fail',
                'message': '用户名密码不匹配'
            }
            return JsonResponse(result)
