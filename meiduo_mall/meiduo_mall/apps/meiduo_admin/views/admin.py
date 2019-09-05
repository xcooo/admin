#! /usr/bin/env python3
# encoding: utf-8
"""
@file: admin.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.group import GroupSerialzier
from users.models import User
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import Group
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

    def simple(self, request):
        """
        获取分组表数据
        :param request:
        :return:
        """
        # 1.获取分组数据
        data = Group.objects.all()

        # 2.序列化返回
        ser = GroupSerialzier(data, many=True)

        return Response(ser.data)