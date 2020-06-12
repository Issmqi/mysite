#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @date: 2020-06-11 
# @name: register
# @author：shimengqi
import json
from django import views
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rbac.forms import formAuth
from myapp import models
from mysite.common.util import log

log=log.Log()

class Register(views.View):
    def get(self, request):
        return render(request, "register.html")
    def post(self,request):
        # data=request.POST
        # log.info('判断参数是否合法')
        # form_obj=formAuth.RegForm(data)
        # if form_obj.is_valid():
        #     valid_data=form_obj.cleaned_data
        #     username=valid_data.get("username")
        #     password=valid_data.get("password")
        #     log.info('username是：%s'%username)
        #     log.info('password是：%s' % password)
        #     #判断user是否已经存在
        #     if models.UserInfo.objects.filter(username=username):
        #         # form_obj.add_error("username","账号已存在")
        #         # return render(request,"register.html",{"form_obj":form_obj})
        #         return HttpResponse("账号已存在")
        #     else:
        #         #账号可用，去掉确认密码，数据写入数据库
        #         # del valid_data["r_password"]
        #         test1 = models.UserInfo(account=username,password=password)
        #         test1.save()#创建新用户
        #         back = {
        #             'status': '200',
        #             'message': '成功'
        #         }
        #         return JsonResponse(back)
        # else:
        #
        #     #数据验证不通过
        #     # return render(request,"register.html",{"form_obj":form_obj})
        #     back = {
        #         'code': '200',
        #         'message': '失败'
        #     }
        #     # back=json.dumps(form_obj)
        #     # return JsonResponse(back)
        #     return render(request, "register.html", {"form_obj": form_obj})

        username=request.POST.get('username')
        password = request.POST.get('password')
        log.info('username的类型是：%s' % type(username))
        log.info('username是：%s' % username)
        log.info('password是：%s' % password)
        test1 = models.UserInfo(account=username, password=password)
        test1.save()  # 创建新用户
        back = {
            'status': '200',
            'message': '成功'
        }
        return JsonResponse(back)




