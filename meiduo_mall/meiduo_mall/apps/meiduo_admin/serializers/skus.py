#! /usr/bin/env python3
# encoding: utf-8
"""
@file: skus.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework import serializers
from goods.models import SKU
from goods.models import GoodsCategory

class SkuSerializer(serializers.ModelSerializer):
    """
    sku序列化器
    """
    class Meta:
        model = SKU
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    分类id序列化器
    """
    class Meta:
        model = GoodsCategory
        fields = '__all__'