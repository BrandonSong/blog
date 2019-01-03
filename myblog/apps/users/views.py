from django.shortcuts import render
from django.views.generic import View
# Create your views here.



class RegisterView(View):
    """ 注册模块 """
    def get(self, request):
        """ 处理get方式请求 返回注册页面"""
        return render(request, "register.html")
