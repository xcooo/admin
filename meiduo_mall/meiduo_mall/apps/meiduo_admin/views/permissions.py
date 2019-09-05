#! /usr/bin/env python3
# encoding: utf-8
"""
@file: permissions.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from meiduo_admin.serializers.permisssions import PermissionSerializer, ContentTypeSerializer
from meiduo_admin.utils import PageNum
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import Permission,ContentType


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

    # 父类中没有权限类型表操作的方法, 需要我们自己封装方法
    def content_type(self, request):
        """
        获取权限类型
        :param request:
        :return:
        """
        # 1.获取权限类型所有数据
        data = ContentType.objects.all()

        # 2.序列化返回多个数据
        ser = ContentTypeSerializer(data, many=True)

        return Response(ser.data)