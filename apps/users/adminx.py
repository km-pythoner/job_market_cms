# -*- coding:utf-8 -*- 
__author__ = 'jiangjun'
__date__ = '2018/3/14 14:29 '

import xadmin
from xadmin import views

from .models import UserProfile


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    site_title = '猎场后台管理系统'
    site_footer = '猎场后台管理系统'
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSettings)


# class UserProfileAdmin(object):
#     list_display = ['username', 'email', 'mobile', 'gender', 'birthday', 'create_time']
#     search_fields = ['username', 'email', 'mobile']
#     list_filter = ['username', 'email', 'mobile', 'gender', 'create_time']
#
# xadmin.site.register(UserProfile, UserProfileAdmin)
