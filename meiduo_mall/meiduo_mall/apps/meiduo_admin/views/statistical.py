#! /usr/bin/env python3
# encoding: utf-8
"""
@file: statistical.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
import datetime
from rest_framework.permissions import IsAdminUser

class UserTotalCountView(APIView):
    """
    用户总量统计
    """
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):

        # 获取当前时间
        date = datetime.date.today()  # 2018-01-17

        # 获取用户数量
        count = User.objects.all().count()

        # 返回结果
        return Response({
            'count':count,
            'date':date
        })


class UsercurrentCountView(APIView):
    """
    日增用户统计
    """
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):

        # 获取当前时间
        date = datetime.date.today()  # 2018-01-17

        # 获取用户数量
        count = User.objects.filter(date_joined__gte=date).count()

        # 返回结果
        return Response({
            'count':count,
            'date':date
        })

class UseractiveCountView(APIView):
    """
    日活跃用户统计
    """
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):

        # 获取当前时间
        date = datetime.date.today()  # 2018-01-17

        # 获取用户数量
        count = User.objects.filter(last_login__gte=date).count()

        # 返回结果
        return Response({
            'count':count,
            'date':date
        })