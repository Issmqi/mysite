#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @date: 2020-06-11 
# @name: register
# @author：shimengqi
from django import views
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rbac.forms import formAuth
from myapp import models



class Register(views.View):
    def get(self, request):
        return render(request, "register.html")
    def post(self,request):
        data=request.POST
        form_obj=formAuth.RegForm(data)
        if form_obj.is_valid():
            valid_data=form_obj.cleaned_data
            username=valid_data.get("username")
            #判断user是否已经存在
            if models.UserInfo.objects.filter(username=username):
                form_obj.add_error("username","账号已存在")
                return render(request,"register.html",{"form_obj":form_obj})
            else:
                #账号可用，去掉确认密码，数据写入数据库
                # del valid_data["r_password"]
                test1 = models.UserInfo(account=valid_data["username"],password=valid_data["password"])
                test1.save()#创建新用户
                back = {
                    'code': '200',
                    'message': '成功'
                }
                return JsonResponse(back)
        else:
            #数据验证不通过
            # return render(request,"register.html",{"form_obj":form_obj})
            back = {
                'code': '200',
                'message': '失败'
            }
            return JsonResponse(back)




