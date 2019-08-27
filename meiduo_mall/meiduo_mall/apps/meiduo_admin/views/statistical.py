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
# from datetime import timedelta
from rest_framework.permissions import IsAdminUser
from orders.models import OrderInfo
from goods.models import GoodsVisitCount
from ..serializers.statistical import GoodsSerializer


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
            'count': count,
            'date': date
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
            'count': count,
            'date': date
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
            'count': count,
            'date': date
        })


class UserordersCountView(APIView):
    """
    日下单用户统计
    """
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当前时间
        date = datetime.date.today()  # 2018-01-17

        # 获取用户数量
        count = len(set(User.objects.filter(orders__create_time__gte=date)))

        # 返回结果
        return Response({
            'count': count,
            'date': date
        })


class UserMonthCountView(APIView):
    """
     月增用户统计
    """
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当前时间
        now_date = datetime.date.today()  # 2018-01-17

        # 获取一个月之前的时间
        begin_date = now_date - datetime.timedelta(days=29)

        # 3.从一个月之前的日期开始遍历循环获取每一天的数据
        date_list = []
        for i in range(30):
            # 起始日期
            index_date = begin_date + datetime.timedelta(days=i)
            # 下一天日期(起始日期的第二天)
            next_date = begin_date + datetime.timedelta(days=i + 1)
            count = User.objects.filter(date_joined__gte=index_date, date_joined__lt=next_date).count()
            date_list.append({
                'count':count,
                'date':index_date
            })

        # 4.返回结果
        return Response(date_list)


class UserGoodCountView(APIView):
    """
    日分类商品访问数量
    """
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当前时间
        date = datetime.date.today()  # 2018-01-17

        # 获取分类访问量数量
        goods = GoodsVisitCount.objects.filter(date__gte=date)

        # 交给序列化器序列化
        ser = GoodsSerializer(goods, many=True)

        # 返回结果
        return Response(ser.data)
