#! /usr/bin/env python3
# encoding: utf-8
"""
@file: permisssions.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework import serializers
from django.contrib.auth.models import Permission

class PermissionSerializer(serializers.ModelSerializer):
    """
    权限类序列化器
    """
    class Meta:
        model = Permission
        fields = '__all__'