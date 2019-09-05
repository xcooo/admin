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

    # 父类保存数据库的方法不满足需求, 需要重写
    def create(self, validated_data):
        user = super(AdminSerialzier, self).create(validated_data)
        user.is_staff = True
        # 密码加密
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        user = super(AdminSerialzier, self).update(instance, validated_data)
        # 密码加密
        user.set_password(validated_data['password'])
        user.save()
        return user