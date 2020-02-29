from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime,timedelta
from django.core.mail import send_mail  #邮件模块
from HHelp.settings import EMAIL_FROM   #导入邮件设置
import random

from h import models

# Create your views here.

#登录函数
def login(request):
    if request.method == 'GET':
        # return HttpResponse('OK')
        return render(request,'login.html')
    elif request.method == 'POST':
        print('接收到post请求')
        #拿到账号和密码，在数据库中进行查询
        u = request.POST.get('username')
        p = request.POST.get('password')
        print("username:"+u)
        print("password:"+p)

        obj = models.user.objects.filter(email=u,password=p).first()
        #print("obj:"+obj)
        print(obj)

        if obj:
            #将用户email存入浏览器的cookie中
            # 设置cookie，根据httpresponse,render,redirect,共有三种方式，根本在于HttpResponse对象
            # obj1.set_cookie()
            # 获取
            # request.COOKIES.get()
            # 删除
            # obj1.delete_cookie()
            response = redirect('/NearbyPharmacy/')
            response.set_cookie('username',u,expires=datetime.now()+timedelta(days=14))
            return redirect('/NearbyPharmacy/')
            #return response
        else:
            print('账号或密码错误')
            return render(request,'login.html')

        #return render(request, 'NearbyPharmacy.html')

        # return redirect('/NearbyPharmacy/')

#注册页面
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')

#验证码界面
def vercode(request):
    if request.method == 'GET':
        print("打印get请求如下：",request)
        email = request.GET.get('email')
        print("email的值如下:",email)
        # if(/^[0-9a-z])
        # if (/ ^[0-9a-zA-Z.-_]+ @[0-9a-zA-Z.-_]+(\.[a-zA-Z]+){1, 2}$ /.test(this.value)):

        email_title = '验证码为：'
        #生成验证码
        str = ""
        for i in range(6):
            ch = chr(random.randrange(ord('0'),ord('9')+1))
            str += ch
        print(str)
        email_body = str    #邮件主题内容为生成的六位随机数验证码

        #将验证码存放在 vercode表中
        models.VerCode.objects.create(email=email,vercode=str)

        #此处的 email应该进行正则表达式的检测
        email2 = email  #发送的邮箱

        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email2]) #发送
        print(send_status)
        if(send_status):
            print("发送成功")
        return HttpResponse(1)

    elif request.method == 'POST':
        print("打印post请求如下：",request)
        return HttpResponse('收到验证码')

#注册账号页面
def registerEmail(request):
    if request.method == 'GET':
        return HttpResponse("get类型的register请求")
    elif request.method == 'POST':
        # email:$('#username').val(),
        # vercode:$('#VerificationCode').val(),
        # password:$('#password').val(),
        # ConfirmPassword:$('#ConfirmPassword').val(),
        email2 = request.POST.get('email')
        vercode2 = request.POST.get('vercode')
        password2 = request.POST.get('password')
        vercode = models.VerCode.objects.filter(email=email2).last().vercode
        print("vercode2:",vercode2)
        if(vercode == vercode2):
            print("注册成功")
            models.user.objects.create(email=email2,password=password2)
            # status = 1
            # return render(request,'register.html',{'status':status})
            return HttpResponse(1)
        else:
            print("注册失败")
            # status = 0
            # return render(request,'register.html',{'status':status})
            return HttpResponse(0)
#附近药房页面
def NearbyPharmacy(request):
    if request.method == 'GET':
        return render(request,'NearbyPharmacy.html')

#食疗养生函数
def Diet_health(request):
    if request.method == 'GET':

        #数据部分
        return render(request,'Diet_health.html')

#医药配方函数
def Pharmaceutical_formula(request):
    if request.method == 'GET':
        return render(request,'Pharmaceutical_formula.html')

#对话专家函数
def Dialogue_expert(request):
    if request.method == 'GET':
        experts_list = []
        experts = models.experts.objects.all()
        print(experts)
        print(experts[1].name)

        count = experts.count()
        print(count)

        for expert in experts:
            print(expert.name)
            #experts_list.append(expert.name)

        return render(request,'Dialogue_expert.html',{'experts':experts,'count':count})

#忌吃清单函数
def Avoid_eating_list(request):
    if request.method == 'GET':
        eating_list = models.ban.objects.all()

        return render(request,'Avoid_eating_list.html',{'eating_list':eating_list})

#运动保健函数
def Sports_health(request):
    if request.method == 'GET':
        articles = models.sport.objects.all()
        return render(request,'Sports_health.html',{'articles':articles})

#在线挂号函数
def Online_registration(request):
    if request.method == 'GET':
        return render(request,'Online_registration.html')

#智能备忘页面
def Smart_notes(request):
    if request.method == 'GET':
        return render(request,'Smart_notes.html')

#个人中心页面
def personalCenter(request):
    if request.method == 'GET':
        return render(request,'personalCenter.html')

#修改密码页面
def changePassword(request):
    if request.method == 'POST':
        #拿到旧密码，新密码，和确认密码
        #1，根据cookie中存储的用户名，将旧密码与数据库中数据进行比较
        #2，比对新密码与确认密码是否相同
        #obj = models.user.objects.filter(email=u,password=p).first()

        op = request.POST.get('oldPassword')    #拿到旧密码

        u = request.COOKIES['username']    #根据cookie中的email去数据库中查询旧密码，进行比较
        print("cookie中的数据：",u)
        pp = models.user.objects.filter(email=u).first().password
        print("数据库中的密码：",pp)

        np = request.POST.get('newPassword')
        cp = request.POST.get('confirmPassword')

        if (op == pp):
            print("旧密码与数据库中密码相同，可以进行新密码与确认密码的比对")
            if(np == cp):
                print('新密码和确认密码相同')
                models.user.objects.filter(email=u).update(password=cp)
                return HttpResponse('修改成功')
            else:
                return HttpResponse("新密码与确认密码不同，请重新输入")
        else:
            return HttpResponse('旧密码错误，请重新输入')
#成为专家页面
def become_epert(request):
    if request.method == 'GET':
        return render(request,'become_epert.html')

#文章阅读页面
def read(request,nid):
    if request.method == 'GET':
        print("nid数字的值为：",nid)
        title = models.sport.objects.filter(id = nid).first().title
        content = models.sport.objects.filter(id = nid).first().content

        return render(request,'read.html',{'title':title,'content':content})