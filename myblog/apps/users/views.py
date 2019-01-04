from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
# Create your views here.



class RegisterView(View):
    """ register module """
    def get(self, request):
        """ method： get
            func: return register.html
        """
        return render(request, "register.html")

    def post(self, request):
        """ method: post
            func: collect user data and generate a User instant
        """
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        print(username, pwd)
        return HttpResponse("注册成功")
