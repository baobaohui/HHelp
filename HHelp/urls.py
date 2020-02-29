"""HHelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path

from h import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login),# 登录界面

    path('register/',views.register),#注册界面
    path('vercode/',views.vercode),#向用户邮箱发送验证码
    path('registerEmail/',views.registerEmail),#用户带着验证码进行注册

    path('NearbyPharmacy/',views.NearbyPharmacy),#附近药房页面
    path('Diet_health/',views.Diet_health),#食疗养生页面
    path('Pharmaceutical_formula/',views.Pharmaceutical_formula),#医药配方页面
    path('Dialogue_expert/',views.Dialogue_expert),#对话专家页面
    path('Avoid_eating_list/',views.Avoid_eating_list),#忌吃清单页面
    path('Sports_health/',views.Sports_health),#运动保健页面
    path('Online_registration/',views.Online_registration),#在线挂号页面
    path('Smart_notes/',views.Smart_notes),#智能备忘页面

    path('personalCenter/',views.personalCenter),#个人中心页面
    path('changePassword/',views.changePassword),#修改密码页面
    path('become_epert/',views.become_epert),#成为专家页面

    re_path('read/(?P<nid>\d+)/',views.read),#文章阅读页面

]
