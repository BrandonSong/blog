from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class UserProfile(models.Model):
    """ 用户数据模型扩展 """
    user = models.OneToOneField(User)  # 与Django自带用户模型建立对应关系
    qq_number = models.CharField(max_length = 16, default = "")  # QQ号登陆时使用
    wechat_number = models.CharField(max_length = 16, default = "")  # 微信号登录时使用
    phone_number = models.CharField(max_length = 16, default = "", validators = [])  # 手机号注册时使用

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.user.name



class Permission(models.Model):
    """ 用户权限模型 """
    name = models.CharField("权限名称", max_length = 64)
    url = models.CharField("URL名称", max_length = 255)

    class Meta:
        verbose_name = "权限表"
        verbose_name_plural = verbose_name
        permissions = (
            ("common", "查看博客"),
            ("operator", "操作博客"),
            ("admin", "网站管理员"),
        )