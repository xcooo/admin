#! /usr/bin/env python3
# encoding: utf-8
"""
@file: permisssions.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework import serializers
from django.contrib.auth.models import Permission,ContentType

class PermissionSerializer(serializers.ModelSerializer):
    """
    权限数据序列化器
    """
    class Meta:
        model = Permission
        fields = '__all__'


class ContentTypeSerializer(serializers.ModelSerializer):
    """
    权限类型序列化器
    """
    name = serializers.CharField(read_only=True) # 指定显示的字段
    class Meta:
        model = ContentType
        fields = '__all__'