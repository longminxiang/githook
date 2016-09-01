# -*- coding: utf-8 -*-
from django.apps import AppConfig

_path = 'apps.Hooker'


class HookerConfig(AppConfig):
    name = _path
    verbose_name = u'githook配置'


default_app_config = '%s.HookerConfig' % _path
