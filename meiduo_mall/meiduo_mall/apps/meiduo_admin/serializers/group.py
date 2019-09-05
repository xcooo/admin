#! /usr/bin/env python3
# encoding: utf-8
"""
@file: group.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework import serializers
from django.contrib.auth.models import Group


class GroupSerialzier(serializers.ModelSerializer):
    """
    分组表序列化器
    """
    class Meta:
        model = Group
        fields = '__all__'