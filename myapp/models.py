from django.db import models

# Create your models here.
# class Stu(models.Model):
#     '''自定义Stu表对应的Model类'''
#     # 定义属性：默认主键自增id字段可不写
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=16)
#     age = models.SmallIntegerField()
#     sex = models.CharField(max_length=1)
#     classid = models.CharField(max_length=8)
#
#     # 定义默认输出格式
#     def __str__(self):
#         return "%d:%s:%d:%s:%s" % (self.id, self.name, self.age, self.sex, self.classid)
#
#     # 自定义对应的表名，默认表名：myapp_stu
#     class Meta:
#         db_table = "stu"


class Test(models.Model):
    name=models.CharField(max_length=20)

class Person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

    def Meta(self):
        db_table='person'


class UserInfo(models.Model):

    objects=models.Manager()
    account=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    create_time=models.DateField(auto_now=True)

    def Meta(self):
        db_table='users'

