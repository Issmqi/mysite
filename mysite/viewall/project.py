#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @date: 2020-07-10 
# @name: project
# @author：shimengqi

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from  myapp.serializers.serializer import ProjectSerializer
from myapp.models import Project
from mysite.common.api_response import JsonResponse

class AddProject(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = ()

    def parameter_check(self,data):
        try:
            # 必传参数 name, version, type
            if not data["project_name"]:
                return JsonResponse(code="999996", msg="关键参数[project_name]缺失！")

        except KeyError:
            return JsonResponse(code="999996", msg="参数错误！")

    def post(self, request):
        """
        新增项目
        :param request:
        :return:
        """
        data = JSONParser().parse(request)
        result = self.parameter_check(data)
        if result:
            return result
        data["user"] = request.user.pk
        project_serializer = ProjectDeserializer(data=data)
        try:
            Project.objects.get(name=data["name"])

            return JsonResponse(code="999997", msg="存在相同名称")
        except ObjectDoesNotExist:
            with transaction.atomic():
                if project_serializer.is_valid():
                    # 保持新项目
                    project_serializer.save()
                    # 记录动态
                    record_dynamic(project=project_serializer.data.get("id"),
                                   _type="添加", operationObject="项目", user=request.user.pk, data=data["name"])
                    # 创建项目的用户添加为该项目的成员
                    self.add_project_member(project_serializer.data.get("id"), request.user.pk)
                    return JsonResponse(data={
                            "project_id": project_serializer.data.get("id")
                        }, code="999999", msg="成功")
                else:
                    return JsonResponse(code="999998", msg="失败")