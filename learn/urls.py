# -*- coding: UTF-8 -*-
from django.conf.urls import url

#from learn import views
from learn import views
urlpatterns = [
    url(r'^delSelect$',views.delSelect,name='delSelect'),
    url(r'delete$', views.delByID, name='delByID'),
    url(r'^show$',views.show,name='show'),
    url(r'^showAll$',views.showAll,name='showAll'),
    url(r'^showAll0$',views.showAll0,name='showAll0'),
    url(r'^showMy$',views.showMy,name='showMy'),
    url(r'^query$',views.queryById,name='queryById'),
    url(r'^queryR$',views.queryByIdR,name='queryByIdR'),
    url(r'^queryM$',views.queryByIdM,name='queryByIdM'),
    url(r'^insertPage$',views.insertPage,name='insertPage'),
    url(r'^add$',views.add,name='add'),
    url(r'delete$',views.delByID,name='delByID'),
    url(r'update$',views.update,name='update'),
    url(r'feedback$',views.feedback,name='feedback'),
    url(r'feedback_handler$',views.feedback_handler,name='feedback_handler'),
    url(r'subscribe$',views.subscribe,name='subscribe'),
    url(r'cancel$',views.cancel,name='cancel'),

]