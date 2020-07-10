#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
# @date: 2020-07-10 
# @name: api_response
# @author：shimengqi
# desc:统一封装接口返回response
'''

from rest_framework.response import Response
from  rest_framework.serializers import Serializer

class JsonResponse(Response):
    def __init__(self,data='',code='',msg='',status='',template_name='', headers='',
                 exception=False, content_type=''):
        super(Response, self).__init__(None, status=status)
        if isinstance(data, Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)
        self.data = {"code": code, "msg": msg, "data": data}
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        # if headers:
        #     for name, value in six.iteritems(headers):
        #         self[name] = value