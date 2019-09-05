#! /usr/bin/env python3
# encoding: utf-8
"""
@file: admin.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework import serializers
from users.models import User

class AdminSerialzier(serializers.ModelSerializer):
    """
    管理员序列化器
    """
    class Meta:
        model = User
        fields = '__all__'
        # 密码只参与反序列化
        extra_kwargs = {
            'password':{
                'write_only':True
            }
        }