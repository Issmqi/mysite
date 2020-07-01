from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from myapp import models
import requests
import json
from rest_framework import viewsets
from myapp.models import UserInfo
from myapp.serializers.user_serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    views_name = "django学习"
    return render(request, 'runoob.html', {"name": views_name})


def test1(request):
    view_list = ['django学习1', 'django学习2', 'django学习3']
    return render(request, 'test.html', {"views_list": view_list})


def test(request):
    url = 'http://192.168.41.16/occ-purchase/purchase/goods-cost-prices/query'
    param = {
        'search_EQ_skuId': '002',
        'search_AUTH_APPCODE': 'goodsCostPrice'
    }
    re = requests.get(url, params=param).json()
    return render(request, 'test.html', {"response": re})


def login_view(request):
    return HttpResponse('hello,this is login')


def get_project(request):
    reportid = request.GET.get("aa")
    print(reportid)
    back = {
        'status': '200',
        'message': '成功'
    }
    return JsonResponse(back)


def post_project(request):
    data = json.loads(request.body.decode())
    print(request.body)
    print(type(data))
    add = models.Person(first_name="mengqi", last_name="shi")
    add.save()
    models.Person.objects.create(first_name="mengqi", last_name="shi")
    back = {
        'code': '200',
        'msg': '成功'
    }
    return JsonResponse(back)


def post(request):
    if request.method == 'POST':  # 当提交表单时
        dic = {}
        # 判断是否传参
        if request.POST:
            a = request.POST.get('a', 0)
            b = request.POST.get('b', 0)
            # 判断参数中是否含有a和b
            if a and b:
                res = a + b
                dic['number'] = res
                dic = json.dumps(dic)
                # return HttpResponse(dic)
                return JsonResponse(dic)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')

    else:
        return HttpResponse('方法错误')


# def register(request):
#     if request.method=='GET':
#         #注册页展示
#         views_name="注册页"
#         return render(request,'register.html',{'name':views_name})
#     if request.method=='POST':
#         account=request.POST.get('account',0)
#         password=request.POST.get('password',0)
#         user=models.Users(account=account,password=password)
#         # user=models.Users(account=request.POST.get('account'),password=request.POST.get('password'))
#         user.save()
#         return HttpResponse('注册成功，三秒后跳转到登陆页面')
#         # return HttpResponseRedirect(reverse('acsign:login'))

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username', 0)
        password = request.POST.get('password', 0)
        user_obj = auth.authenticate(username=username,
                                     password=password)  # 这里auth模块拿到用户名和密码后，会去auth_user表中查找数据，如果存在返回用户对象，不存在返回None
        if user_obj:
            auth.login(request, user_obj)
            # 1.auth.login做了session的事情，将用户数据存入数据库，生成sessionid存在cookie中
            # 2.request.user=user_obj，将用户对象存在请求中的user中。
            return HttpResponse('登录成功')
        else:
            return HttpResponse('用户名或密码不存在')


# @login_required()
def home(request):
    # return render(request,'home.html')
    return HttpResponse("接口自动化测试平台")
