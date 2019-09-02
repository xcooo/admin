#! /usr/bin/env python3
# encoding: utf-8
"""
@file: skus.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework import serializers
from goods.models import SKU, SPUSpecification, SpecificationOption
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


class SpecOptionSerializer(serializers.ModelSerializer):
    '''
    规格选项序列化器
    '''
    class Meta:
        model = SpecificationOption
        fields = '__all__'


class SPUSpecSerializer(serializers.ModelSerializer):
    """
    规格序列化器
    """
    # 嵌套序列化返回规格选项 (如果指定 related_name, 就不能使用 模型类名小写_set)
    options = SpecOptionSerializer(many=True)
    # specificationoption_set = SpecOptionSerializer(many=True)

    class Meta:
        model = SPUSpecification
        fields = '__all__'