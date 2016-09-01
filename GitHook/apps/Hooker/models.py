# -*- coding: utf-8 -*-
from django.db import models


class ProjectInfo(models.Model):
    '''
    git项目信息
    '''

    name = models.CharField(max_length=128, unique=True, verbose_name="名称")

    summary = models.CharField(max_length=512, blank=True, verbose_name="描述")

    git_url = models.CharField(max_length=256, verbose_name="git地址")

    project_path = models.CharField(default='/home/git', max_length=256, verbose_name="项目路径")

    use_rsa = models.BooleanField(default=False, verbose_name='是否使用rsa')

    rsa_pri_key = models.TextField(blank=True, verbose_name="rsa key")

    is_active = models.BooleanField(default=True, verbose_name='是否激活')

    @property
    def git_host(self):
        host = self.git_url.split('@')[1]
        host = host.split(':')[0]
        return host

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'git项目信息'
        verbose_name_plural = verbose_name
