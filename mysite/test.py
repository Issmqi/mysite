#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @date: 2020-06-24 
# @name: test
# @author：shimengqi
import requests
import json
header={
    'Content-Type':'application/json',
    'charset':'UTF-8'
}
url='http://localhost:8000/api/v1/user/register/'
param={
    'username':'test2',
    'password':'123456'
}

params=json.dumps(param)
re=requests.post(url=url,data=param)
print(re.content)
print(re.json())