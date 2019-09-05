#! /usr/bin/env python3
# encoding: utf-8
"""
@file: orders.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework import serializers

from goods.models import SKU
from orders.models import OrderInfo, OrderGoods


class SkuSerializer(serializers.ModelSerializer):
    '''
    商品图片,名称序列化器
    '''
    class Meta:
        model = SKU
        fields = ('name', 'default_image')


class OrderGoodsSerializer(serializers.ModelSerializer):
    """
    订单商品序列化器
    """
    # 嵌套序列化返回商品图片和名称信息
    sku = SkuSerializer(read_only=True)

    class Meta:
        model = OrderGoods
        fields = ('price', 'count', 'sku')


class OrderSerializer(serializers.ModelSerializer):
    """
    订单序列化器
    """
    # 嵌套序列化返回订单商品信息
    # 注意,嵌套两层以上序列化器时, 只需要在最下面加 many=True
    skus = OrderGoodsSerializer(read_only=True, many=True)

    class Meta:
        model = OrderInfo
        fields = '__all__'