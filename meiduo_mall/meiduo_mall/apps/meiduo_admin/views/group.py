#! /usr/bin/env python3
# encoding: utf-8
"""
@file: group.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from django.contrib.auth.models import Group
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from meiduo_admin.serializers.group import GroupSerialzier
from meiduo_admin.utils import PageNum


class GroupView(ModelViewSet):
    """
    用户组管理
    """
    # 指定查询集
    queryset = Group.objects.all()

    # 指定序列化器
    serializer_class = GroupSerialzier

    # 指定分页器
    pagination_class = PageNum

    # 指定权限
    permission_classes = [IsAdminUser]