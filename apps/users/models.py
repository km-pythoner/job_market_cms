from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
        用户消息
    """
    GENDER_TYPE = (
        ('M', '男'),
        ('F', '女')
    )
    birthday = models.DateField('出生日期', null=True, blank=True)
    gender = models.CharField('性别', max_length=1, choices=GENDER_TYPE, default='M')
    mobile = models.CharField('联系电话', max_length=11, null=True, blank=True)
    email = models.EmailField('邮箱', max_length=30, null=True, blank=True)
    profile_picture = models.ImageField('用户头像', upload_to='user/%Y/%m', default='user/default-profile.jpg')
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    update_time = models.DateTimeField('更新时间', default=datetime.now)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        db_table = 'user_profile'

    def __str__(self):
        return self.username
