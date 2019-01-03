# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='权限名称', max_length=64)),
                ('url', models.CharField(verbose_name='URL名称', max_length=255)),
            ],
            options={
                'permissions': (('', '查看博客'), ('', '操作博客'), ('', '网站管理员')),
                'verbose_name_plural': '权限表',
                'verbose_name': '权限表',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('qq_number', models.CharField(max_length=16, default='')),
                ('wechat_number', models.CharField(max_length=16, default='')),
                ('phone_number', models.CharField(max_length=16, default='')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '用户表',
                'verbose_name': '用户表',
            },
        ),
    ]
