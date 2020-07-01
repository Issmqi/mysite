#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @date: 2020-06-15 
# @name: myserializers.py
# @author：shimengqi

from rest_framework import serializers
from . import models

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        models = models.UserInfo
        fields = '__all__'



# user,goods为表名

#
# class GoodsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = models.Goods
#         fields = '__all__'
