#! /usr/bin/env python3
# encoding: utf-8
"""
@file: images.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from django.conf import settings
from fdfs_client.client import Fdfs_client

from rest_framework import serializers
from rest_framework.response import Response

from goods.models import SKUImage
from goods.models import SKU

class ImageSerializer(serializers.ModelSerializer):
    """
    图片序列化器
    """
    class Meta:
        model = SKUImage
        fields = '__all__'

    def create(self, validated_data):
        # 3.建立fastdfs的客户端
        client = Fdfs_client(settings.FASTDFS_PATH)

        # 4.上传upload图片
        # self.context['request']  # 获取request对象

        image = self.context['request'].FILES.get('image')
        res = client.upload_appender_by_buffer(image.read())  # 文件byte数据

        # 5.判断图片是否上传成功
        if res['Status'] != 'Upload successed.':
            raise serializers.ValidationError({'error':'图片上传失败'})

        # 6.保存图片表
        sku = validated_data['sku']  # 验证后的数据是一个对象
        img = SKUImage.objects.create(sku_id=sku.id, image=res['Remote file_id'])
        return img


class ImageIdSerializer(serializers.ModelSerializer):
    '''
    图片id序列化器
    '''
    class Meta:
        model = SKU
        fields = ('id','name')