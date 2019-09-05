#! /usr/bin/env python3
# encoding: utf-8
"""
@file: orders.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser

from meiduo_admin.serializers.orders import OrderSerializer
from meiduo_admin.utils import PageNum
from orders.models import OrderInfo


class OrderView(ReadOnlyModelViewSet):

    # 指定查询集
    queryset = OrderInfo.objects.all()

    # 指定序列化器
    serializer_class = OrderSerializer

    # 指定分页器
    pagination_class = PageNum

    # 指定权限
    permission_classes = [IsAdminUser]

    # 重写获取查询集数据的方法
    def get_queryset(self):
        if self.request.query_params.get('keyword') == '':
            return OrderInfo.objects.all()
        elif self.request.query_params.get('keyword') is None:
            return OrderInfo.objects.all()
        else:
            return OrderInfo.objects.filter(order_id__contains=self.request.query_params.get('keyword'))
