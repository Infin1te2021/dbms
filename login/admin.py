from django.contrib import admin
from django.contrib.auth.models import Group, User
# Register your models here.

from . import models

admin.site.register(models.Author)
admin.site.register(models.Reader)

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = '系统后台'
admin.site.site_title = '后台'