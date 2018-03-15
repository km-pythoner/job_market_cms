from datetime import datetime

from django.db import models

# Create your models here.


class CityDict(models.Model):
    city_name = models.CharField('城市名称', max_length=20)
    city_desc = models.CharField('城市描述', max_length=200)
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField('更新时间', default=datetime.now)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name
        db_table = 'city_dict'

    def __str__(self):
        return self.city_name


class CompanyInfo(models.Model):
    BUSSINESS_TYPE = (
        ('1', '互联网/电子商务'),
        ('2', '金融/投资/证券'),
        ('3', '房地产')
    )
    company_name = models.CharField('企业名称', max_length=30)
    company_location = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name='企业所在地')
    business_category = models.CharField('行业分类', max_length=1, choices=BUSSINESS_TYPE)
    profile_picture = models.ImageField('企业头像', upload_to='employer/%Y/%m', default='employer/default-profile.jpg')
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    update_time = models.DateTimeField('更新时间', default=datetime.now)

    class Meta:
        verbose_name = '企业信息'
        verbose_name_plural = verbose_name
        db_table = 'company_info'

    def __str__(self):
        return self.company_name


class JobInfo(models.Model):
    job_name = models.CharField('职位名称', max_length=20)
    deploy_company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, verbose_name='发布企业')
    job_location = models.ForeignKey(CityDict ,on_delete=models.CASCADE,verbose_name='工作地点')
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    update_time = models.DateTimeField('更新时间', default=datetime.now)

    class Meta:
        verbose_name = '职位信息'
        verbose_name_plural = verbose_name
        db_table = 'job_info'

    def __str__(self):
        return self.job_name


class JobApply(models.Model):
    job_info = models.ForeignKey(JobInfo, on_delete=models.CASCADE, verbose_name='职位信息')
    employee_info = models.ForeignKey
