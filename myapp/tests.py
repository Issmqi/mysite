from django.test import TestCase

# Create your tests here.
import json
import requests
url='http://localhost:8000/api/v1/user/auth/login/'
# header={
#     'Content-Type': 'application/json'
# }

header={
    'Content-Type': 'application/json'
    # 'Content-Type': 'application/x-www-form-urlencoded'
    # 'Content-Type': 'multipart/form-data'
}
param={
    'username':'admin',
    'password':'admin123'
}

params=json.dumps(param)

re=requests.post(url,data=params,headers=header)
# re=requests.post(url,data=param,headers=header)
#data:a=1&b=2
#json:'{"a": 1, "b": 2}
print(re.content)
print(re.json())
