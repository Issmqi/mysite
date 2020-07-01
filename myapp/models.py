from django.db import models

from pygments.lexers import get_all_lexers  # 一个实现代码高亮的模块
from pygments.styles import get_all_styles
import django.utils.timezone as timezone

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])  # 得到所有编程语言的选项
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())  # 列出所有配色风格


class Test(models.Model):
    name = models.CharField(max_length=20)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def Meta(self):
        db_table = 'person'


class UserInfo(models.Model):
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


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
