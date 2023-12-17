# -*- coding: utf-8 -*- 
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from login import views
from django.views import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index_v1/', views.index_v1),
    url(r'^$', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^pagejump/', views.pagejump),
    url(r'^captcha', include('captcha.urls')),
    url(r'^user_center/', views.userviews, name="user_center"),
    url(r'^user_centerA/', views.userviewsA, name="user_centerA"),
    url(r'^learn/', include('learn.urls', namespace='learn')),
    url(r'^static/(?P<path>.*)$', static.serve,
      {'document_root': settings.STATIC_ROOT}, name='static'),
    # 设置media路由
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
]

handler404 = views.page_not_found
handler500 = views.page_error