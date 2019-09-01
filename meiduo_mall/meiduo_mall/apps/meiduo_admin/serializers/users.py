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
        fields = ('id','username','mobile','email')