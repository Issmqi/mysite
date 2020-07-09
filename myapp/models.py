from django.db import models

from pygments.lexers import get_all_lexers  # 一个实现代码高亮的模块
from pygments.styles import get_all_styles
import django.utils.timezone as timezone

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])  # 得到所有编程语言的选项
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())  # 列出所有配色风格

REQUEST_PARAMETER_TYPE_CHOICE = (
    ('form-data', '表单(form-data)'),
    ('parameter', 'parameter'),
    ('body', 'body')
)
REQUEST_TYPE_CHOICE=(
    ('post','post'),
    ('put','put'),
    ('get','get'),
    ('delete','delete')

)

def update_last_login(sender, user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])


class UserInfo(models.Model):
    '''用户信息'''
    objects = models.Manager()
    id = models.CharField(primary_key=True, max_length=50, verbose_name='用户编号')

    username = models.CharField(max_length=30, verbose_name='用户名')
    password = models.CharField(max_length=30, verbose_name='密码')
    email = models.CharField(max_length=30, verbose_name='邮箱', blank=True)
    create_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', blank=True)
    # last_login = models.DateTimeField(verbose_name='最近登录',blank=True)
    is_superuser = models.CharField(max_length=10, verbose_name='是否超级用户', default='0')
    first_name = models.CharField(max_length=30, verbose_name='名字', blank=True)
    last_name = models.CharField(max_length=30, verbose_name='姓氏', blank=True)
    is_active = models.CharField(max_length=30, verbose_name='是否激活', default='1')

    def Meta(self):
        db_table = 'user_info'  ## 表在数据库的名字
        verbose_name = '用户信息表'  # 在admin站点显示名称
        verbose_name_plural = verbose_name

#
# class Project(models.Model):
#     '''项目信息'''
#     objects = models.Manager()
#     project_id = models.AutoField(primary_key=True, verbose_name='项目id')
#     project_name = models.CharField(max_length=50, verbose_name='项目名称')
#     time = models.DateTimeField(auto_now=True, max_length=50, verbose_name='操作时间')
#     type = models.CharField(max_length=50, verbose_name='操作类型')
#     operationObject = models.CharField(max_length=50, verbose_name='操作对象')
#     user = models.ForeignKey(UserInfo, related_name='username', blank=True, null=True,
#                              on_delete=models.SET_NULL, verbose_name='操作人')
#     description = models.CharField(max_length=1024, blank=True, null=True, verbose_name='描述')
#
#     def __unicode__(self):
#         return self.project_id
#
#     def __str__(self):
#         return self.project_id
#
#     class Meta:
#         data_table = 'project'
#         verbose_name = '项目'
#         verbose_name_plural = verbose_name
#
#
# class ApiGroup(models.Model):
#     '''
#     接口分组
#     '''
#
#     objects = models.Manager()
#     group_id = models.AutoField(primary_key=True, verbose_name='接口分组id')
#     project = models.ForeignKey(Project, related_name='project_id', on_delete=models.CASCADE, verbose_name='所属项目')
#     group_name = models.CharField(max_length=50, verbose_name='接口分组名称')
#
#     def __unicode__(self):
#         return self.group_id
#
#     def __str__(self):
#         return self.group_id
#
#     class Meta:
#         data_table = 'group'
#         verbose_name = '接口分组'
#         verbose_name_plural = verbose_name
#
#
# class ApiInfo(models.Model):
#     '''接口信息'''
#     objects = models.Manager()
#     api_id = models.AutoField(primary_key=True, verbose_name='接口id')
#     project = models.ForeignKey(Project, related_name="project_id", on_delete=models.CASCADE, verbose_name='所属项目')
#     api_group = models.ForeignKey(ApiGroup, related_name="group_id", blank=True, null=True, on_delete=models.SET_NULL,
#                                   verbose_name='所属分组')
#     api_name=models.CharField(max_length=50,verbose_name='接口名称')
#     param_type=models.CharField(max_length=50,verbose_name='')
#
#
# class AutoTestCase(models.Model):
#     '''用例信息'''
#     objects=models.Manager()
#     case_id=models.AutoField(primary_key=True,verbose_name='用例编号')
#     case_name=models.CharField(max_length=50,verbose_name='用例名称')
#     header=models.CharField(max_length=120,verbose_name='请求头')
#     path=models.CharField(max_length=1024,verbose_name="请求路径")
#     request_type=models.CharField(max_length=120,verbose_name='请求类型')
#     param_type=models.CharField(max_length=50,verbose_name='请求擦数类型')
#     param=models.TextField(verbose_name='请求参数')
#     expect_code=models.CharField(max_length=10,verbose_name='预期状态码')
#     actul_code=models.CharField(max_length=10,verbose_name='实际状态码')
#     expect_result=models.TextField(verbose_name='预期结果')
#     actul_result=models.TextField(verbose_name='实际结果')
#     is_depend=models.CharField(verbose_name='是否依赖case')
#     depend_case_id=models.CharField(verbose_name='依赖的caseid')
#
#
