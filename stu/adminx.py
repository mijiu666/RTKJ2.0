#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Date: 2019/10/8 0008 17:45
# Author: Mijiu
# Version: 1.0
import xadmin
from stu.models import StudentInfo
from xadmin import views


# 然后我们需要创建class，class命名格式最好为类名+Admin
class RtStudentAdmin:
    list_display = ['no', 'name', 'gender', 'age', 'city']
    list_fields = ['no','name','gender','age','city','school_name']
    search_fields = ['no', 'name', 'gender', 'age', 'city', 'school_name']
    list_editable = ['name', 'gender', 'age', 'city','school_name']
    ordering = ['age']

class GlobalSetting(object):
    site_title = '人通学生管理系统'  # 设置头标题
    site_footer = '人通学生管理系统'  # 设置脚标题
    menu_style = 'accordion'  # 可收缩列


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(StudentInfo, RtStudentAdmin)