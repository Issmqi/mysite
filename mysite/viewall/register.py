#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @date: 2020-06-11 
# @name: register
# @author：shimengqi
import json
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from myapp.serializers import user_serializers
from mysite.common.util import log


class User(APIView):

    def post(self, request):
        '''注册用户'''
        serializer = user_serializers.UserSerializer(data=request.data)
        if serializer.is_valid():

            log.Log().info('请求数据是%s' % serializer)
            username = serializer.validated_data.get('username','')
            password = serializer.validated_data.get('password','')
            log.Log().info('用户名是%s' % username)
            log.Log().info('密码是%s' % password)
            if not username:
                content = {
                    'status': False,
                    'msg': '用户名不正确'
                }
                return JsonResponse(data=content, status=status.HTTP_200_OK)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request):
    #     '''查询用户'''
    #     # 获取auth中的用户
    #     user = request.user
    #     if user.is_authenticated:  # is_superuser
    #         return HttpResponse(user.username + '已授权')
    #     return HttpResponse('未授权')
