# __author__: liqinsong
# data: 2019/1/3

from django.conf.urls import url
from users.views import RegisterView


urlpatterns = [
    url(r'^register/', RegisterView.as_view(), name="register"),  # 用户模块
]