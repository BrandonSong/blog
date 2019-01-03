# __author__: liqinsong
# data: 2019/1/3
from django.conf import settings
from django.core.mail import send_mail


def send_register_active_email(to_email, username, token):
    """ 发送激活邮件 """
    subject = "新用户激活"
    message = ""
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    html_message = '<h1>%s,欢迎您注册成为黎勤松个人博客的用户</h1>请点击下面的链接激活您的账号<br>' \
                   '<a href="http://127.0.0.1:8000/user/active/%s">' \
                   'http://127.0.0.1:8000/user/active/%s</a>' % (username, token, token)

    send_mail(subject, message, sender, receiver, html_message = html_message)