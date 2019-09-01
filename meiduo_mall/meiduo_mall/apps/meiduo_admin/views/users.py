#! /usr/bin/env python3
# encoding: utf-8
"""
@file: users.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework.generics import ListAPIView

from meiduo_admin.serializers.users import UserSerializer
from meiduo_admin.utils import PageNum
from users.models import User


class UserView(ListAPIView):
    """
    获取用户数据
    """
    # 使用分页器
    pagination_class = PageNum
    # 指定查询集
    queryset = User.objects.all()
    # 指定序列化器
    serializer_class = UserSerializer