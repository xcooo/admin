#! /usr/bin/env python3
# encoding: utf-8
"""
@file: images.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework import serializers
from goods.models import SKUImage
from goods.models import SKU

class ImageSerializer(serializers.ModelSerializer):
    """
    图片序列化器
    """
    class Meta:
        model = SKUImage
        fields = '__all__'


class ImageIdSerializer(serializers.ModelSerializer):
    '''
    图片id序列化器
    '''
    class Meta:
        model = SKU
        fields = ('id','name')