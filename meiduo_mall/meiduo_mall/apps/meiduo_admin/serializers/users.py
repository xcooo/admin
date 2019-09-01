#! /usr/bin/env python3
# encoding: utf-8
"""
@file: users.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','mobile','email', 'password') # id默认是read_only

        extra_kwargs = {
            'password':{
                'write_only':True,
                'max_length':20,
                'min_length':6,
            },

            'username': {
                'max_length': 20,
                'min_length': 3,
            }
        }

    # 密码需要加密, 需要重写create方法(两种方法)
    def create(self, validated_data):
        # user = super().create(validated_data)
        # # 密码加密的方法
        # user.set_password(validated_data['password'])
        # user.save()

        # 第二种方法, 管理器方法
        user = User.objects.create_user(**validated_data)
        return user