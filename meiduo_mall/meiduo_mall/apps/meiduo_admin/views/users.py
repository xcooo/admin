#! /usr/bin/env python3
# encoding: utf-8
"""
@file: users.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework.generics import ListCreateAPIView

from meiduo_admin.serializers.users import UserSerializer
from meiduo_admin.utils import PageNum
from users.models import User


class UserView(ListCreateAPIView):
    """
    获取用户数据(单个和多个, 在同一个url路径请求下)
    """
    # 使用分页器
    pagination_class = PageNum
    # 指定查询集  (重写后就不需要指定)
    # queryset = User.objects.all()
    # 指定序列化器
    serializer_class = UserSerializer


    # 重写获取查询集数据的方法
    def get_queryset(self):
        if self.request.query_params.get('keyword') == '':
            return User.objects.all()
        else:
            return User.objects.filter(username__contains=self.request.query_params.get('keyword'))