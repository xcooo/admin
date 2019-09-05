#! /usr/bin/env python3
# encoding: utf-8
"""
@file: admin.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework.viewsets import ModelViewSet
from users.models import User
from rest_framework.permissions import IsAdminUser

from meiduo_admin.serializers.admin import AdminSerialzier
from meiduo_admin.utils import PageNum


class AdminView(ModelViewSet):
    """
    管理员视图
    """
    # 指定序列化器
    serializer_class = AdminSerialzier

    # 指定查询集
    queryset = User.objects.filter(is_staff=True)

    # 指定分页器
    pagination_class = PageNum

    # 指定权限
    permission_classes = [IsAdminUser]