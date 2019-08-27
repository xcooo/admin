from django.contrib.auth.backends import ModelBackend
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin
from django.http import HttpRequest
import re
from users.models import User


class MeiduoModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if request is None:
            # 后台登陆 判断是否为管理员
            try:
                # is_superuser 判断用户是否为超级管理员
                user = User.objects.get(username=username, is_superuser=True)
            except:
                return None

            if user is not None and user.check_password(password):
                return user
        else:
            try:
                # if re.match(r'^1[3-9]\d{9}$', username):
                #     user = User.objects.get(mobile=username)
                # else:
                #     user = User.objects.get(username=username)
                user = User.objects.get(username=username)
            except:
                # 如果未查到数据，则返回None，用于后续判断
                try:
                    user = User.objects.get(mobile=username)
                except:
                    return None
                    # return None

            # 判断密码和用户是否存在
            if user.check_password(password):
                return user
            else:
                return None

