# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt

from . import models
from login.models import Author,Reader
from .forms import UserForm, RegisterForm
import hashlib

def index(request):
    if request.session.get('is_login', None):
        return render(request, 'index.html')
    else:
        return redirect("/login/")
def index_v1(request):
    return render(request, 'index_v1.html')
def pagejump(request):
    return render(request, 'pagejump.html')
@csrf_exempt
def login(request):
    if request.session.get('is_login', None):
        return redirect("/")
    if request.method == "POST":
        login_form = UserForm(request.POST)
        print(login_form)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            user_role = login_form.cleaned_data['user_role']
            userID = login_form.cleaned_data['userID']
            password = login_form.cleaned_data['password']
            print(user_role,userID,password)
            if user_role=='0':
                try:
                    user = models.Reader.objects.get(readerId=userID)
                    if user.password == password:  # 哈希值和数据库内的值进行比对
                        request.session['is_login'] = True
                        request.session['user_qx'] = False
                        request.session['user_id'] = user.readerId
                        request.session['user_name'] = user.readerName
                        return redirect('/')
                    else:
                        message = "密码不正确！"
                except:
                    message = "该账户不存在！"
            elif user_role=='1':
                try:
                    user = models.Author.objects.get(authorId=userID)
                    if user.password == password:  # 哈希值和数据库内的值进行比对
                        request.session['is_login'] = True
                        request.session['user_qx'] = True
                        request.session['user_id'] = user.authorId
                        request.session['user_name'] = user.authorName
                        return redirect('/')
                    else:
                        message = "密码不正确！"
                except:
                    message = "账户不存在！"
            else:
                print("user_role-error")
        return render(request, 'login.html', locals())
    login_form = UserForm()
    return render(request, 'login.html', locals())
@csrf_exempt
def register(request):
    if request.session.get('is_login', None):
        return redirect("/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            user_role = register_form.cleaned_data['user_role']
            nickname = register_form.cleaned_data['nickname']
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            phone = register_form.cleaned_data['phone']
            sex = register_form.cleaned_data['sex']
            if user_role == '0':
                if password1 != password2:
                    message = "两次输入的密码不同！"
                    return render(request, 'register.html', locals())
                else:
                    same_name_user = models.Reader.objects.filter(readerId=username)
                    if same_name_user:
                        message = '用户已经存在，请重新输入！'
                        return render(request, 'register.html', locals())
                    same_phone_user = models.Reader.objects.filter(phone=phone)
                    if same_phone_user:
                        message = '该手机号已被注册，请使用别的手机号！'
                        return render(request, 'register.html', locals())
                    new_user = models.Reader.objects.create()
                    new_user.readerId = username
                    new_user.readerName = nickname
                    new_user.password = password1
                    new_user.phone = phone
                    new_user.sex = sex
                    new_user.save()
                    return redirect('/pagejump/')
            elif user_role == '1':
                if password1 != password2:
                    message = "两次输入的密码不同！"
                    return render(request, 'register.html', locals())
                else:
                    same_name_user = models.Author.objects.filter(authorId=username)
                    if same_name_user:
                        message = '用户已经存在，请重新输入！'
                        return render(request, 'register.html', locals())
                    same_phone_user = models.Author.objects.filter(phone=phone)
                    if same_phone_user:
                        message = '该手机号已被注册，请使用别的手机号！'
                        return render(request, 'register.html', locals())
                    new_user = models.Author.objects.create()
                    new_user.authorId = username
                    new_user.authorName = nickname
                    new_user.password = password1
                    new_user.phone = phone
                    new_user.sex = sex
                    new_user.save()
                    return redirect('/pagejump/')
            else:
                pass
    register_form = RegisterForm()
    return render(request, 'register.html', locals())



def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    request.session.flush()
    return redirect('/login/')


def hash_code(s, salt='mysite_login'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

def userviews(request):
    user_id = request.session['user_id']
    reader = Reader.objects.get(readerId=user_id)
    return render_to_response('usercenter-info.html',{'data':reader})
def userviewsA(request):
    user_id = request.session['user_id']
    author = Author.objects.get(authorId=user_id)
    return render_to_response('usercenter-infoA.html',{'data':author})
def page_not_found(request):
    return render_to_response('404.html')

def page_error(request):
    return render_to_response(request, '500.html')
