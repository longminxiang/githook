# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hooker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('git_url', models.CharField(max_length=256, verbose_name=b'git\xe5\x9c\xb0\xe5\x9d\x80')),
                ('project_path', models.CharField(default=b'/home/git', max_length=256, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe8\xb7\xaf\xe5\xbe\x84')),
                ('use_rsa', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xbd\xbf\xe7\x94\xa8rsa')),
                ('rsa_pri_key', models.TextField(verbose_name=b'rsa key', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\xbf\x80\xe6\xb4\xbb')),
            ],
            options={
                'verbose_name': 'githook\u914d\u7f6e\u4fe1\u606f',
                'verbose_name_plural': 'githook\u914d\u7f6e\u4fe1\u606f',
            },
        ),
    ]
