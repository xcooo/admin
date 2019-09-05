#! /usr/bin/env python3
# encoding: utf-8
"""
@file: group.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from django.contrib.auth.models import Group, Permission
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from meiduo_admin.serializers.group import GroupSerialzier
from meiduo_admin.serializers.permisssions import PermissionSerializer
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

    def simple(self, request):
        """
        获取用户组权限
        :param request:
        :return:
        """
        # 1.查询权限表
        data = Permission.objects.all()

        # 2.序列化器返回数据
        ser = PermissionSerializer(data, many=True)

        return Response(ser.data)