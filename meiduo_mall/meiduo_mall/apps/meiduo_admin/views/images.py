#! /usr/bin/env python3
# encoding: utf-8
"""
@file: images.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from goods.models import SKUImage, SKU
from meiduo_admin.serializers.images import ImageSerializer, ImageIdSerializer
from meiduo_admin.utils import PageNum
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


class ImagesViewset(ModelViewSet):
    """
    spu图片管理
    """
    # 指定模型类
    queryset = SKUImage.objects.all()
    # 指定序列化器
    serializer_class = ImageSerializer

    # 指定分页器
    pagination_class = PageNum

    # 指定权限
    permission_classes = [IsAdminUser]


    @action(methods=['GET'],detail=True)
    def simple(self, request):
        """
        图片id获取
        """
        ids = SKU.objects.all()
        ser = ImageIdSerializer(ids, many=True)
        return Response(ser.data)