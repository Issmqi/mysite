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


class Login():
    def get(self, request):
        return render(request, "login.html")

    def post(self,request):
        data=request.POST

        username=data.get("username")
        password=data.get("password")

        user=auth.authenticate(username=username,password=password)
        if user:
            #将用户名存入session
            request.session['user']=username
            auth.login(request,user)#将用户信息存入session
            result={'status':'2'}
            return JsonResponse(result)
        else:
            return JsonResponse({'status':'3'})