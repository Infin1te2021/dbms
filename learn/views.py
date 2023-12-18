# -*- coding: UTF-8 -*-
import datetime

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from learn.models import Learn,Goods,supplier
from login.models import Author,Reader

def insertPage(request):
    return render_to_response('learn/insert.html')
@csrf_exempt
# def add(request):
#     user_id = request.session['user_id']
#     author = Author.objects.get(authorId=user_id)
#     aa = Learn.objects.filter(authorId=author)
#     id=request.POST['id']
#     title=request.POST['title']
#     subscribeNum=request.POST['subscribeNum']
#     feedback=request.POST['feedback']
#     content=request.POST['describe']
#     status=request.POST['status']
#     dt = datetime.datetime.now()
#     cl=Learn()
#     if  len(id)  > 0 :
#        cl.id=id
#     cl.authorId=author
#     cl.title=title
#     cl.subscribeNum=subscribeNum
#     cl.feedback=feedback
#     cl.content=content
#     cl.status=status
#     cl.c_time=dt
#     cl.save()
#     return HttpResponseRedirect("/learn/show")
#重写后的Add
def add(request):
    id=request.POST['id']
    name=request.POST['name']
    category=request.POST['category']
    brand=request.POST['brand']
    price=request.POST['price']
    description = request.POST['description']
    quantity = request.POST['quantity']
    sid = supplier.objects.filter(sid=request.POST['sid']).first()
    cl=Goods()
    cl.id=id
    cl.name=name
    cl.category=category
    cl.brand=brand
    cl.price=price
    cl.description=description
    cl.quantity=quantity
    cl.sid=sid
    cl.save()
    return HttpResponseRedirect("/learn/show")
# def delSelect(request):
#      arr = request.GET['arr']
#      bb = str(arr).split(',')
#      cc = [i for i in bb if i != '']
#      cc = tuple(map(int, cc))
#      if len(cc) ==1:
#         blist = "(" + bb[-1] + ")"
#         Learn.objects.extra(where=['id IN ' + str(blist) + '']).delete()
#      else:
#         Learn.objects.extra(where=['id IN '+str(cc)+'']).delete()
#      return HttpResponse("delect success")

#重写批量删除
def delSelect(request):
    arr = request.GET['arr']
    bb = str(arr).split(',')
    cc = [i for i in bb if i != '']
    cc = tuple(map(int, cc))
    if len(cc) == 1:
        blist = "(" + bb[-1] + ")"
        Goods.objects.extra(where=['id IN ' + str(blist) + '']).delete()
    else:
        Goods.objects.extra(where=['id IN ' + str(cc) + '']).delete()
    return HttpResponse("delect success")
# def show(request):
#     limit = 10
#     user_id=request.session['user_id']
#     author=Author.objects.get(authorId=user_id)
#     aa = Learn.objects.filter(authorId=author)
#     paginator = Paginator(aa, limit)
#     page = request.GET.get('page')
#     try:
#         aa = paginator.page(page)
#     except PageNotAnInteger:
#         aa = paginator.page(1)
#     except EmptyPage:
#         aa = paginator.page(paginator.num_pages)
#     return render_to_response('learn/curdA.html', {'data':aa})
#重写后的show
def show(request):
    limit = 10
    user_id=request.session['user_id']
    author=Author.objects.get(authorId=user_id)
    #aa = Learn.objects.filter(authorId=author)
    aa = Goods.objects.all()
    paginator = Paginator(aa, limit)
    page = request.GET.get('page')
    try:
        aa = paginator.page(page)
    except PageNotAnInteger:
        aa = paginator.page(1)
    except EmptyPage:
        aa = paginator.page(paginator.num_pages)
    return render_to_response('learn/curdA.html', {'data':aa})
# def show(request):
#     data = Goods.objects.all()
#     return render(request, 'show.html', {'data': data})

def showAll(request):
    limit = 10
    aa = Learn.objects.get_queryset().order_by('id')
    paginator = Paginator(aa, limit)
    page = request.GET.get('page')
    try:
        aa = paginator.page(page)
    except PageNotAnInteger:
        aa = paginator.page(1)
    except EmptyPage:
        aa = paginator.page(paginator.num_pages)
    return render_to_response('learn/curdAll.html',{'data':aa})



def showAll0(request):
    limit = 10
    aa = Goods.objects.get_queryset().order_by('id')
    paginator = Paginator(aa, limit)
    page = request.GET.get('page')
    try:
        aa = paginator.page(page)
    except PageNotAnInteger:
        aa = paginator.page(1)
    except EmptyPage:
        aa = paginator.page(paginator.num_pages)
    return render_to_response('learn/curdR.html', {'data':aa})
def showMy(request):
    limit = 10
    user_id=request.session['user_id']
    reader=Reader.objects.get(readerId=user_id)
    aa=reader.subscribe.all()
    paginator = Paginator(aa, limit)
    page = request.GET.get('page')
    try:
        aa = paginator.page(page)
    except PageNotAnInteger:
        aa = paginator.page(1)
    except EmptyPage:
        aa = paginator.page(paginator.num_pages)
    return render_to_response('learn/curdMy.html', {'data':aa})
def queryById(request):
    id=request.GET['id']
    if id == "":
       return HttpResponseRedirect("/learn/show")
    bb=Learn.objects.filter(id=id)
    return render_to_response('learn/curdA.html', {'data':bb})

def queryByIdR(request):
    id=request.GET['id']
    if id == "":
       return HttpResponseRedirect("/learn/showAll0")
    bb=Learn.objects.filter(id=id)
    return render_to_response('learn/curdR.html', {'data':bb})

def queryByIdM(request):
    id=request.GET['id']
    if id == "":
       return HttpResponseRedirect("/learn/showMy")
    bb=Learn.objects.filter(id=id)
    return render_to_response('learn/curdMy.html', {'data':bb})

# def update(request):
#     id=request.GET['id']
#     bb=Learn.objects.get(id=id)
#     return render_to_response('learn/update.html',{'data':bb})
#重写update方法
def update(request):
    id=request.GET['id']
    bb=Goods.objects.get(id=id)
    return render_to_response('learn/update.html',{'data':bb})
def feedback(request):
    id=request.GET['id']
    bb=Learn.objects.get(id=id)
    return render_to_response('learn/feedback.html',{'data':bb})
@csrf_exempt
def feedback_handler(request):
    id = request.POST['id']
    feedback = request.POST['feedback']
    feedback_old = request.POST['feedback_old']
    user_id = request.session['user_id']
    reader = Reader.objects.get(readerId=user_id)
    cc = Learn.objects.get(id=id)
    new_feedback=feedback_old+'\n'+feedback+'------'+reader.readerId
    cc.feedback=new_feedback
    cc.save()
    return HttpResponseRedirect("/learn/showAll0")

# def delByID(request):
#     id=request.GET['id']
#     bb=Learn.objects.get(id=id)
#     bb.delete()
#     return HttpResponseRedirect("/learn/show")
#重写的单个删除
def delByID(request):
    id=request.GET['id']
    bb=Goods.objects.get(id=id)
    bb.delete()
    return HttpResponseRedirect("/learn/show")
def subscribe(request):
    user_id = request.session['user_id']
    reader = Reader.objects.get(readerId=user_id)
    arr = request.GET['arr']
    bb=str(arr).split(',')
    cc = [i for i in bb if i != '']
    cc = list(map(int, cc))
    for i in cc :
        Learn.objects.get(id=i)
        x = Learn.objects.get(id=i)
        x.subscribeNum += 1
        x.save()
        reader.subscribe.add(Learn.objects.get(id=i))
    return HttpResponse("subscribe success")
def cancel(request):
    user_id = request.session['user_id']
    reader = Reader.objects.get(readerId=user_id)
    arr = request.GET['arr']
    bb=str(arr).split(',')
    cc = [i for i in bb if i != '']
    cc = list(map(int, cc))
    for i in cc :
        reader.subscribe.remove(Learn.objects.get(id=i))
        x=Learn.objects.get(id=i)
        x.subscribeNum-=1
        x.save()
    return HttpResponse("cancel success")

