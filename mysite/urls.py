"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views, testdb
from views.account import Login

urlpatterns = [

    path('runoob/', views.runoob),
    path('user/get/', views.get_project),
    path('user/post/', views.post_project),
    # path('api/v1/user/auth/login/create/', views.login, name="login"),
    path('login/', views.login, name="login"),
    path('api/v1/user/auth/register/', views.register),
    path('home/', views.home, name="home"),
    path('testdb/', testdb.testdb),
    path('test/', views.test),
    path('test/post/', views.post),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login_view),  # 根目录
    url(r'^myapp/', include('myapp.urls')),

]
