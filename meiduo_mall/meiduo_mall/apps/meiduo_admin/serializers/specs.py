#! /usr/bin/env python3
# encoding: utf-8
"""
@file: specs.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework import serializers
from goods.models import SPUSpecification
from goods.models import SPU

class SpecsSerializer(serializers.ModelSerializer):
    """
    商品spu的序列化器
    """
    # 指定关联外键返回形式
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()
    class Meta:
        model = SPUSpecification
        fields = '__all__'


class SpuSerializer(serializers.ModelSerializer):
    """
    spu商品序列化器
    """
    class Meta:
        model = SPU
        fields = ('id','name')