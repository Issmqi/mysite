#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
# @date: 2020-06-24
# @name: user_serializers
# @author：shimengqi

'''

from rest_framework import serializers
from myapp.models import UserInfo
import uuid


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)  # 指定需要序列化的数据
    username = serializers.CharField(required=True, max_length=30)
    password = serializers.CharField(required=True, max_length=30)
    # linenos = serializers.DateField(required=False)

    email = serializers.CharField(required=False,max_length=30,)
    # create_time = serializers.DateField(auto_now=True)
    # update_time = serializers.DateTimeField(required=False)
    # last_login = serializers.DateField(required=False)
    # is_superuser = serializers.CharField(max_length=10,default='0')
    first_name = serializers.CharField(required=False,max_length=30)
    last_name = serializers.CharField(required=False, max_length=30)
    # is_active = serializers.CharField(max_length=30)

    class Meta:
        model = UserInfo
        fields = '__all__'
        # extra_kwargs={
        #     "id": {"read_only":True,"required":False},#主键系统生成
        #     "username":{"required":True},
        #     "password":{"required":True},
        #     "create_time":{"required":False}
        # }

    def create(self, validated_data):
        validated_data["id"] = uuid.uuid4()  # 添加一个唯一的uuid作为主键
        return UserInfo.objects.create(**validated_data)

    def get(self):
        pass
