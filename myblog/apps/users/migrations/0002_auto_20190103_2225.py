# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permission',
            options={'verbose_name': '权限表', 'verbose_name_plural': '权限表', 'permissions': (('common', '查看博客'), ('operator', '操作博客'), ('admin', '网站管理员'))},
        ),
    ]
