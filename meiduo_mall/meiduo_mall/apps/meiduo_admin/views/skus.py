#! /usr/bin/env python3
# encoding: utf-8
"""
@file: skus.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from goods.models import SKU
from meiduo_admin.serializers.skus import SkuSerializer, CategorySerializer
from meiduo_admin.utils import PageNum
from rest_framework.permissions import IsAdminUser
from goods.models import GoodsCategory



class SkuView(ModelViewSet):
    """
    获取sku数据(单个和多个, 在同一个url路径请求下)
    """
    # 指定序列化器
    serializer_class = SkuSerializer

    # 指定查询集  (重写后就不需要指定)
    queryset =  SKU.objects.all()

    # 指定分页器
    pagination_class = PageNum

    # 指定权限类
    permission_classes = [IsAdminUser]

    @action(methods=['get'], detail=False)
    def categories(self, request):
        """
        获取商品三级分类
        """
        data = GoodsCategory.objects.filter(subs__id=None)
        ser = CategorySerializer(data, many=True)
        return Response(ser.data)