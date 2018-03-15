# -*- coding:utf-8 -*- 
__author__ = 'jiangjun'
__date__ = '2018/3/15 15:00 '

import xadmin

from .models import CityDict, CompanyInfo, JobInfo


class CityDictAdmin(object):
    list_display = ['city_name', 'city_desc', 'create_time']
    search_fields = ['city_name']
    list_filter = ['city_name', 'city_desc', 'create_time']


xadmin.site.register(CityDict, CityDictAdmin)


class CompanyInfoAdmin(object):
    list_display = ['company_name', 'company_location', 'business_category', 'create_time']
    search_fields = ['company_name', 'company_location', 'business_category', 'create_time']
    list_filter =  ['company_name', 'company_location', 'business_category', 'create_time']


xadmin.site.register(CompanyInfo, CompanyInfoAdmin)


class JobInfoAdmin(object):
    list_display = ['job_name', 'deploy_company', 'job_location', 'create_time']
    search_fields = ['job_name', 'deploy_company', 'job_location']
    list_filter = ['job_name', 'deploy_company', 'job_location']


xadmin.site.register(JobInfo, JobInfoAdmin)
