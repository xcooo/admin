#! /usr/bin/env python3
# encoding: utf-8
"""
@file: permissions.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.permisssions import PermissionSerializer
from meiduo_admin.utils import PageNum
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import Permission


class PermissionsView(ModelViewSet):
    """
    权限管理视图
    """
    # 指定查询集
    queryset = Permission.objects.all()

    # 指定序列化器
    serializer_class = PermissionSerializer

    # 指定分页器
    pagination_class = PageNum

    # 指定权限
    permission_classes = [IsAdminUser]