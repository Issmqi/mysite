#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @date: 2020-07-10 
# @name: project_serializers
# @author：shimengqi

from rest_framework import serializers
from myapp.models import Project
import uuid

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'