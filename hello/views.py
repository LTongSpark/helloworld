from django.shortcuts import render
from django.http import HttpResponse ,Http404 ,JsonResponse
from . import models
from django.core import serializers
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail

import json
# Create your views here.

def index(request):
    return HttpResponse("hello wprd")

def hello(request):
    return render(request ,'hello/hello.html')

def demo(request):
    return render(request, 'hello/demo.html')

def page(request ,num):
    try:
        num  = int(num)
        return render(request ,'hello/demo.html')
    except:
        return Http404

def home(request ,year = "2019" ,month = "01"):
    return HttpResponse("当前页面的时间为：{}年/{}月".format(year ,month))

def name(request ):
    return render(request ,'hello/name.html' ,{'name':"tong"})

#向数据库添加数据

def add(request):
    text = models.text(name="tong")
    text.save()
    return  HttpResponse("save sucess")

#注册数据
def regist(request):
    user = models.User(user_name="tong" ,pword="123456789" ,emil="liutongsparl@163.com")
    user.save()
    return HttpResponse("save sucess")

#更新数据
def update(request):
    models.User.objects.filter(user_name="tong").update(pword = "123Q")
    return HttpResponse("update sucess")

#删除数据

def delete(request):
    models.User.objects.filter(user_name="tong").delete()
    return HttpResponse("delete sucess")

#查询数据
def select(request):
    m = models.User.objects.get(user_name="tong")
    return HttpResponse("select =>{},{},{}".format(m.user_name,m.pword,m.emil))

def select_all(request):
    r = ""
    m = models.User.objects.values('user_name' ,'emil','pword')
    for i in m:
        r += str(i)
    return HttpResponse("select_all =>{}".format(r))

def get_json(request):
    '''返回json数据'''
    data = {}
    result = models.User.objects.all()
    json.dumps()
    data["result"] = json.loads(serializers.serialize('json',result))
    return JsonResponse(data ,safe=False ,json_dumps_params={'ensure_ascii' :False})

def test_qq(request):
    return render(request,'hello/qq.html')

def result(request):
    '''返回结果'''
    if request.method.upper() == 'get':
        #获取提取到的数据
        r = request.GET.get('qq' ,None)
        print(r)
        res = ""
        try:
            if int(r) %2:
                res = "偶数"
            else:
                res = "奇数"
        except:
            res = "请输入正确的QQ号"
        return HttpResponse("测试结果：{}".format(res))
    else:
        render(request ,"hello/qq.html")

#从数据库中查询数据到页面

def user(request):
    '''请求页面-返回结果'''
    res = ""
    if request.method == 'GET':
        # 获取提交的数据
        n = request.GET.get('name', None)  # key不存在时不会报错
        print("result{}".format(n))
        res = models.User.objects.filter(user_name="{}".format(n))
        try:
            res = res[0].emil
        except:
            res = "未查询到数据"
        return render(request, 'hello/name.html', {'emil': res})
    else:
        return render(request, 'hello/name.html', {'emil': res})

def register(request):
    '''注册页面'''
    res = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        psw = request.POST.get('password')
        print("psw{}".format(psw))
        mail = request.POST.get('mail')

        #先在数据库中查是否有这个用户
        user_lst = models.User.objects.filter(user_name=username)
        if user_lst:
            #表示已经注册过 ，给个提示显示这个用户已经注册过
            res = "{}用户已经注册过".format(username)
            return render(request ,'hello/register.html' ,{'rename':res})
        else:
            #无注册过的用户
            user = models.User()
            user.user_name = username
            user.pword = psw
            #加密
            #user.pword = make_password(psw)
            user.emil = mail
            user.save()

            return render(request,'hello/login.html',{'rename':res})
    return render(request, 'hello/register.html')

def login(request):
    '''登录页面'''
    if request.method == "GET":
        return render(request, 'hello/login.html')
    if request.method == "POST":
        # 先查询数据库是否有此用户名
        username = request.POST.get('username')
        psw = request.POST.get('password')
        # 查询用户名和密码
        user_obj = models.User.objects.filter(user_name=username, pword=psw).first()

        #解密
        # ret = models.User.objects.filter(user_name=username).first()
        # chunk_psw = check_password(psw ,ret.pword)
        #if chunk_psw:
        if user_obj:
            return HttpResponse('登陆成功')
        else:
            return HttpResponse('用户名或密码错误')


#修改密码
def reset_pwd(request):
    '''修改密码'''
    res = ""
    if request.method == "GET":
        return render(request ,'hello/reset_psw.html' ,{'msg':res})
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        new_pwd = request.POST.get('new')

        if pwd == new_pwd:
            res = "新密码和旧密码不能一样"
            return render(request, 'hello/reset_psw.html', {'msg': res})
        else:
            #先查询数据库中有无此用户
            user= models.User.objects.filter(user_name=username)
            if user:
                user = models.User.objects.filter(user_name=username).first()
                if user.pword == pwd:
                    user = models.User()
                    user.pword = new_pwd
                    user.save()
                    res = "密码修改成功"
                else:
                    res = "密码错误"
                return render(request, 'hello/reset_psw.html', {'msg': res})
            else:
                res = "用户没有注册：{}".format(username)
                return render(request, 'hello/reset_psw.html', {'msg': res})

#邮件发送

def mail(request):
    send_mail(subject = 'Subject here' , #主题
              message = 'Here is the message.',  # 正文
              from_email ='286702310@qq.com',  # 发件人
              recipient_list = ['liutongspark@163.com'],  # 收件人
              fail_silently=True
              )
    return HttpResponse('邮件发送成功，收不到就去垃圾箱找找吧！')


