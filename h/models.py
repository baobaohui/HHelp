from django.db import models
from django.utils import timezone
# Create your models here.

#user 用户表
class user(models.Model):
    id = models.AutoField(verbose_name="用户id，自增",primary_key=True)
    email = models.EmailField(verbose_name="用户账号，唯一",unique=True)
    password = models.CharField(verbose_name="账号密码",max_length=20)
    isDoctor = models.IntegerField(verbose_name="是否是医生，0：是，1：否",null=True)
    lastlogin = models.DateField(verbose_name="最后登录时间",default=timezone.now)
    token = models.CharField(verbose_name="token,唯一",max_length=40,unique=True)
    vercode = models.CharField(verbose_name="验证码",max_length=6)

#验证码表
class VerCode(models.Model):
    id = models.AutoField(verbose_name="用户id，自增，计数作用",primary_key=True)
    email = models.EmailField(verbose_name="发送验证码的邮箱",max_length=30)
    vercode = models.CharField(verbose_name="随机的验证码",max_length=6)

#专家表
class experts(models.Model):
    id = models.AutoField(verbose_name="专家id，自增", primary_key=True)
    name = models.CharField(verbose_name="专家姓名",max_length=20)
    gender = models.CharField(verbose_name="专家性别", max_length=4)
    keywords = models.CharField(verbose_name="主治类别，骨科之类", max_length=40)

#对话内容表
class conversationList(models.Model):
    id = models.AutoField(verbose_name="此条对话的id，自增", primary_key=True)
    userId = models.IntegerField(verbose_name="用户id，对话双方",null=True)
    expertId = models.IntegerField(verbose_name="专家id，对话双方",null=True)
    content = models.CharField(verbose_name="对话内容", max_length=1024)

#忌吃清单表
class ban(models.Model):
    id = models.AutoField(verbose_name="主键，自增", primary_key=True)
    title = models.CharField(verbose_name="病名，唯一",null=True,max_length=128,unique=True)
    content = models.CharField(verbose_name="内容", max_length=2048)

#运动保健表
class sport(models.Model):
    id = models.AutoField(verbose_name="主键，自增", primary_key=True)
    title = models.CharField(verbose_name="文章名称",null=True,max_length=128)
    content = models.CharField(verbose_name="文章内容", max_length=3072)
    pub_user = models.ForeignKey('user',on_delete=models.CASCADE)#verbose_name="关联自user_id,发布者id",
    pub_time = models.DateField(verbose_name="发布时间",default=timezone.now)
    click_num = models.IntegerField(verbose_name="点击量",null=True)


